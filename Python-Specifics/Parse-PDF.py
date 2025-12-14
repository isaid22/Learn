import asyncio
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List, Optional, Tuple

from pydantic import BaseModel, Field, ValidationError, validator


class RawTerm(BaseModel):
	term: str
	value: str


class NormalizedTerm(BaseModel):
	term: str
	raw_value: str
	normalized_value: Any
	value_type: str = Field(..., description="Type of normalized value: date|currency|string|number")


class Conflict(BaseModel):
	term: str
	values: List[str]
	resolution: str


class ExtractionReport(BaseModel):
	terms: List[NormalizedTerm]
	conflicts: List[Conflict]


# --- Normalization helpers ---
DATE_FORMATS = [
	"%B %d, %Y",  # December 22, 2028
	"%b %d, %Y",  # Dec 22, 2028
	"%Y-%m-%d",
	"%m/%d/%Y",
]


def normalize_date(value: str) -> Optional[str]: # Return ISO format date string or nothing - Optional
	v = value.strip() # remove leading/trailing spaces
	for fmt in DATE_FORMATS:
		try:
			dt = datetime.strptime(v, fmt)
			return dt.date().isoformat()
		except ValueError:
			continue
	return None


def normalize_currency(value: str) -> Optional[Decimal]:
	v = value.strip().replace(",", "")
	if v.startswith("$"):
		v = v[1:]
	try:
		return Decimal(v)
	except InvalidOperation:
		return None


def normalize_number(value: str) -> Optional[Decimal]:
	v = value.strip().replace(",", "")
	try:
		return Decimal(v)
	except InvalidOperation:
		return None


def normalize_value(term: str, value: str) -> Tuple[Any, str]:
	t = term.lower()
	# Heuristics by term name
	if "date" in t:
		d = normalize_date(value)
		if d is not None:
			return d, "date"
	if any(k in t for k in ["amount", "principal", "price", "currency"]):
		c = normalize_currency(value)
		if c is not None:
			return c, "currency"
	# Fallbacks by content
	d = normalize_date(value)
	if d is not None:
		return d, "date"
	n = normalize_number(value)
	if n is not None:
		return n, "number"
	return value.strip(), "string"


# --- Async ETL TermExtractor ---
class TermExtractor:
	def __init__(self, raw_terms: List[Dict[str, str]]):
		self.raw_terms = raw_terms

	async def extract(self) -> ExtractionReport:
		# E: Extract raw -> RawTerm
		raw_items = await self._extract_raw()
		# T: Transform -> NormalizedTerm
		normalized_items = await self._transform(raw_items)
		# L: Load-like step -> detect conflicts and build report
		conflicts = await self._detect_conflicts(normalized_items)
		return ExtractionReport(terms=normalized_items, conflicts=conflicts)

	async def _extract_raw(self) -> List[RawTerm]:
		async def build(item: Dict[str, str]) -> RawTerm:
			await asyncio.sleep(0)  # yield control
			return RawTerm(**item)

		tasks = [build(item) for item in self.raw_terms]
		return await asyncio.gather(*tasks)

	async def _transform(self, raw_items: List[RawTerm]) -> List[NormalizedTerm]:
		async def normalize(item: RawTerm) -> NormalizedTerm:
			await asyncio.sleep(0)
			norm, value_type = normalize_value(item.term, item.value)
			return NormalizedTerm(term=item.term, raw_value=item.value, normalized_value=norm, value_type=value_type)

		tasks = [normalize(item) for item in raw_items]
		return await asyncio.gather(*tasks)

	async def _detect_conflicts(self, items: List[NormalizedTerm]) -> List[Conflict]:
		# group by term
		groups: Dict[str, List[NormalizedTerm]] = {}
		for it in items:
			groups.setdefault(it.term, []).append(it)

		conflicts: List[Conflict] = []
		for term, group in groups.items():
			# If multiple entries for same term with differing normalized values, it's a conflict
			unique_values = {str(g.normalized_value) for g in group}
			if len(unique_values) > 1:
				# resolution policy: prefer the most structured type: date > currency > number > string
				order = {"date": 3, "currency": 2, "number": 1, "string": 0}
				winner = max(group, key=lambda g: order.get(g.value_type, 0))
				resolution = f"Resolved to {winner.normalized_value} ({winner.value_type})"
				conflicts.append(
					Conflict(term=term, values=[g.raw_value for g in group], resolution=resolution)
				)
		return conflicts


async def run_demo():
	data = [
		{"term": "Maturity Date", "value": "December 22, 2028"},
		{"term": "Stated Principal Amount", "value": "$1,000"},
		# Example duplicates to demonstrate conflict detection
		{"term": "Maturity Date", "value": "12/22/2028"},
		{"term": "Stated Principal Amount", "value": "$1000"},
	]
	extractor = TermExtractor(data)
	report = await extractor.extract()
	return report


def main():
	try:
		report = asyncio.run(run_demo())
	except (ValidationError, Exception) as e:
		print(f"Error: {e}")
		return

	print("Normalized Terms:")
	for t in report.terms:
		print(f"- {t.term}: raw='{t.raw_value}' -> {t.normalized_value} [{t.value_type}]")

	if report.conflicts:
		print("\nConflicts:")
		for c in report.conflicts:
			print(f"- {c.term}: inputs={c.values} | {c.resolution}")
	else:
		print("\nNo conflicts detected.")


if __name__ == "__main__":
	main()
