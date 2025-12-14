## ETL Basics
This page is dedicated to ETL basics. The code for reference is [Parse-PDF.py](./Parse-PDF.py). 

Here are some omportant libraries:
```python
from datetime import datetime
from decimal import Decimal, InvalidOperation
from typing import Any, Dict, List, Optional, Tuple
```

We will start with a simple example of given data in such format:

```bash
[
		{"term": "Maturity Date", "value": "December 22, 2028"},
		{"term": "Stated Principal Amount", "value": "$1,000"},
		# Example duplicates to demonstrate conflict detection
		{"term": "Maturity Date", "value": "12/22/2028"},
		{"term": "Stated Principal Amount", "value": "$1000"},
	]
```

The task is to create a program that demostrates how ETL may be done. 

### Data Structure
Declare a class to handle the input data:

```python
from pydantic import BaseModel, Field, ValidationError

class RawTerm(BaseModel):
	term: str
	value: str
```

This is a class defined to handle the input data structure. 

There is a need to normalize data. Date format is a frequent occurence for such scenario:

```python
def normalize_date(value: str) -> Optional[str]: # Return ISO format date string or nothing - Optional
	v = value.strip() # remove leading/trailing spaces
	for fmt in DATE_FORMATS:
		try:
			dt = datetime.strptime(v, fmt)
			return dt.date().isoformat()
		except ValueError:
			continue
	return None
```

Another need for normalization is currency:

```python
def normalize_currency(value: str) -> Optional[Decimal]:
	v = value.strip().replace(",", "") # remove leading/trailing spaces, thousand separator
	if v.startswith("$"):
		v = v[1:]
	try:
		return Decimal(v)
	except InvalidOperation:
		return None
```

This function takes input that is a string (value: str), and may produce output as a decimal if applicable (Optional[Decimal]):

```python
def normalize_currency(value: str) -> Optional[Decimal]:
```

Then it strips trailing and leading spaces if any, and remove comma if it exists as a separator for thousand:

```python
v = value.strip().replace(",", "") # remove leading/trailing spaces, thousand separator
	if v.startswith("$"):
		v = v[1:]
```




### Template
In general, one may use the following template which consists of various pieces or modules. `asyncio` module in Python is routinely used because it enables you to write seemingly concurrent (technically it's a single-threaded, single-process technique known as cooperative multitasking) code using `async` and `await` keywords.

```python
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
```



