from typing import List


def count_ways(amount: int, coins: List[int]) -> int:
	"""Return the number of combinations of coins that sum to amount."""
	# dp[i] holds the number of ways to form total i using processed coins.
	dp = [0] * (amount + 1)
	dp[0] = 1

	for coin in coins:
		for total in range(coin, amount + 1):
			dp[total] += dp[total - coin]

	return dp[amount]


if __name__ == "__main__":  # Simple manual check.
	examples = [
		(5, [1, 2, 5], 4),
		(3, [2], 0),
		(10, [10], 1),
		(0, [1, 2, 3], 1),
	]

	for target, coins, expected in examples:
		result = count_ways(target, coins)
		print(f"amount={target}, coins={coins} -> {result} (expected {expected})")
