"""
LeetCode 70: Climbing Stairs
Dynamic Programming Problem

Problem:
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps.
In how many distinct ways can you climb to the top?

Key Insight:
To reach step n, you can either:
1. Come from step (n-1) and take 1 step
2. Come from step (n-2) and take 2 steps

Therefore: ways(n) = ways(n-1) + ways(n-2)
This is the Fibonacci sequence!

Base cases:
- ways(1) = 1 (only one way: take 1 step)
- ways(2) = 2 (two ways: 1+1 or 2)
"""

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        Optimized solution using O(1) space
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        
        This is the BEST solution for this problem!
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # For n >= 3, we use the recurrence relation
        # We only need to keep track of the last 2 values
        prev2 = 1  # ways(1) = number of ways to reach stair 1
        prev1 = 2  # ways(2) = number of ways to reach stair 2
        
        # Build up from step 3 to step n
        for i in range(3, n + 1):
            current = prev1 + prev2
            # Shift the window
            prev2 = prev1
            prev1 = current # return prev1 as the latest current value, therefore the final result.
        
        return prev1
    
    def climbStairs_dp_array(self, n: int) -> int:
        """
        Dynamic Programming with array (tabulation)
        
        Time Complexity: O(n)
        Space Complexity: O(n)
        
        Good for understanding, but uses more space than necessary.
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Create DP array
        dp = [0] * (n + 1)
        dp[1] = 1
        dp[2] = 2
        
        # Fill the array using recurrence relation
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
    
    def climbStairs_recursive_memo(self, n: int) -> int:
        """
        Recursive solution with memoization (top-down DP)
        
        Time Complexity: O(n)
        Space Complexity: O(n) - for recursion stack + memo dictionary
        
        Good for understanding recursion, but has stack overhead.
        """
        memo = {}
        
        def climb(steps):
            # Base cases
            if steps == 1:
                return 1
            if steps == 2:
                return 2
            
            # Check memo
            if steps in memo:
                return memo[steps]
            
            # Recursive relation
            memo[steps] = climb(steps - 1) + climb(steps - 2)
            return memo[steps]
        
        return climb(n)
    
    def climbStairs_recursive_naive(self, n: int) -> int:
        """
        Naive recursive solution (WITHOUT memoization)
        
        Time Complexity: O(2^n) - EXPONENTIAL! Very slow!
        Space Complexity: O(n) - recursion stack depth
        
        ⚠️ DO NOT USE FOR LARGE n - This will time out!
        Only for educational purposes to show why DP is needed.
        """
        # Base cases
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Recursive relation - recalculates same values many times!
        return self.climbStairs_recursive_naive(n - 1) + self.climbStairs_recursive_naive(n - 2)


def explain_intuition():
    """Explain the intuition behind the solution"""
    print("🧗 CLIMBING STAIRS - INTUITION")
    print("=" * 50)
    print()
    
    print("💡 KEY INSIGHT:")
    print("To reach step n, you must come from either:")
    print("  1. Step (n-1) → take 1 step")
    print("  2. Step (n-2) → take 2 steps")
    print()
    
    print("Therefore:")
    print("  ways(n) = ways(n-1) + ways(n-2)")
    print()
    
    print("📊 BUILDING UP THE SOLUTION:")
    print("-" * 50)
    
    for i in range(1, 8):
        if i == 1:
            print(f"n = {i}: {1} way")
            print("  → [1]")
        elif i == 2:
            print(f"n = {i}: {2} ways")
            print("  → [1,1] or [2]")
        else:
            # Calculate
            prev2 = 1
            prev1 = 2
            for j in range(3, i + 1):
                current = prev1 + prev2
                prev2 = prev1
                prev1 = current
            
            print(f"n = {i}: {prev1} ways")
            print(f"  → ways({i-1}) + ways({i-2}) = {prev1}")
        print()
    
    print("🔍 PATTERN RECOGNITION:")
    print("This is the Fibonacci sequence!")
    print("1, 2, 3, 5, 8, 13, 21, 34, 55, 89...")
    print()


def visualize_solution(n: int):
    """Visualize how the solution builds up"""
    print(f"🎨 VISUALIZING SOLUTION FOR n = {n}")
    print("=" * 50)
    print()
    
    if n == 1:
        print("Step 1:")
        print("  └─ [1]")
        print()
        print("Total: 1 way")
        return
    
    if n == 2:
        print("Step 2:")
        print("  ├─ [1, 1]")
        print("  └─ [2]")
        print()
        print("Total: 2 ways")
        return
    
    if n == 3:
        print("Step 3:")
        print("  ├─ [1, 1, 1]")
        print("  ├─ [1, 2]")
        print("  └─ [2, 1]")
        print()
        print("Total: 3 ways")
        return
    
    # For larger n, show the calculation
    print("Building up step by step:")
    print()
    
    prev2 = 1
    prev1 = 2
    
    print(f"Step 1: 1 way")
    print(f"Step 2: 2 ways")
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        print(f"Step {i}: {current} ways (= {prev1} + {prev2})")
        prev2 = prev1
        prev1 = current
    
    print()
    print(f"✅ Total ways to climb {n} steps: {prev1}")
    print()


def compare_approaches():
    """Compare different solution approaches"""
    print("⚖️  COMPARING DIFFERENT APPROACHES")
    print("=" * 50)
    print()
    
    print("┌─────────────────────┬──────────┬──────────┬─────────────┐")
    print("│ Approach            │ Time     │ Space    │ Recommended │")
    print("├─────────────────────┼──────────┼──────────┼─────────────┤")
    print("│ Naive Recursion     │ O(2^n)   │ O(n)     │ ❌ Never    │")
    print("│ Recursion + Memo    │ O(n)     │ O(n)     │ ⚠️  OK      │")
    print("│ DP Array            │ O(n)     │ O(n)     │ ⚠️  OK      │")
    print("│ Optimized (2 vars)  │ O(n)     │ O(1)     │ ✅ Best     │")
    print("└─────────────────────┴──────────┴──────────┴─────────────┘")
    print()
    
    print("💡 EXPLANATION:")
    print()
    
    print("1️⃣  Naive Recursion (O(2^n) time):")
    print("   - Recalculates same values many times")
    print("   - For n=40, does ~2^40 = 1 trillion operations!")
    print("   - Will TIME OUT on LeetCode")
    print()
    
    print("2️⃣  Recursion + Memoization (O(n) time, O(n) space):")
    print("   - Caches results to avoid recalculation")
    print("   - Still has recursion stack overhead")
    print("   - Good for understanding top-down approach")
    print()
    
    print("3️⃣  DP Array (O(n) time, O(n) space):")
    print("   - Bottom-up approach, easy to understand")
    print("   - Stores all intermediate results")
    print("   - Good for learning DP concepts")
    print()
    
    print("4️⃣  Optimized with 2 Variables (O(n) time, O(1) space):")
    print("   - Only keeps last 2 values (prev1, prev2)")
    print("   - Minimal memory usage")
    print("   - ⭐ BEST solution for this problem!")
    print()


def test_all_approaches():
    """Test all approaches with examples"""
    print("🧪 TESTING ALL APPROACHES")
    print("=" * 50)
    print()
    
    solution = Solution()
    test_cases = [1, 2, 3, 4, 5, 10, 20]
    
    for n in test_cases:
        print(f"n = {n}:")
        
        result1 = solution.climbStairs(n)
        result2 = solution.climbStairs_dp_array(n)
        result3 = solution.climbStairs_recursive_memo(n)
        
        # Only test naive recursion for small n (it's too slow!)
        if n <= 10:
            result4 = solution.climbStairs_recursive_naive(n)
            all_match = result1 == result2 == result3 == result4
            print(f"  Optimized: {result1}")
            print(f"  DP Array: {result2}")
            print(f"  Recursion+Memo: {result3}")
            print(f"  Naive Recursion: {result4}")
        else:
            all_match = result1 == result2 == result3
            print(f"  Optimized: {result1}")
            print(f"  DP Array: {result2}")
            print(f"  Recursion+Memo: {result3}")
            print(f"  Naive Recursion: [skipped - too slow]")
        
        if all_match:
            print(f"  ✅ All approaches match!")
        else:
            print(f"  ❌ Results don't match!")
        print()


def trace_optimized_solution(n: int):
    """Trace through the optimized solution step by step"""
    print(f"🔍 STEP-BY-STEP TRACE: Optimized Solution for n = {n}")
    print("=" * 50)
    print()
    
    if n == 1:
        print("Base case: n = 1")
        print("Return 1")
        return
    
    if n == 2:
        print("Base case: n = 2")
        print("Return 2")
        return
    
    print("Initial setup:")
    print("  prev2 = 1  (ways to reach step 1)")
    print("  prev1 = 2  (ways to reach step 2)")
    print()
    
    prev2 = 1
    prev1 = 2
    
    print("Loop from i = 3 to n:")
    for i in range(3, n + 1):
        current = prev1 + prev2
        print(f"  i = {i}:")
        print(f"    current = prev1 + prev2 = {prev1} + {prev2} = {current}")
        print(f"    prev2 = prev1 = {prev1}")
        print(f"    prev1 = current = {current}")
        
        prev2 = prev1
        prev1 = current
        print()
    
    print(f"✅ Final answer: {prev1}")
    print()


def explain_why_fibonacci():
    """Explain why this problem is the Fibonacci sequence"""
    print("🤔 WHY IS THIS THE FIBONACCI SEQUENCE?")
    print("=" * 50)
    print()
    
    print("📐 FIBONACCI SEQUENCE:")
    print("F(1) = 1")
    print("F(2) = 1")
    print("F(n) = F(n-1) + F(n-2)")
    print()
    print("Sequence: 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...")
    print()
    
    print("🪜 CLIMBING STAIRS:")
    print("ways(1) = 1")
    print("ways(2) = 2")
    print("ways(n) = ways(n-1) + ways(n-2)")
    print()
    print("Sequence: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89...")
    print()
    
    print("🎯 THE CONNECTION:")
    print("Climbing Stairs is shifted Fibonacci by 1 position!")
    print("  ways(n) = F(n+1)")
    print()
    print("Comparison:")
    print("  Fibonacci:       1,  1,  2,  3,  5,  8, 13, 21...")
    print("  Climbing Stairs: 1,  2,  3,  5,  8, 13, 21, 34...")
    print("                   ↑   ↑   ↑   ↑   ↑   ↑   ↑   ↑")
    print("  Index (n):       1   2   3   4   5   6   7   8")
    print()
    print("✅ ways(n) = Fibonacci(n+1)")
    print()


if __name__ == "__main__":
    # Explain the intuition
    explain_intuition()
    
    # Show why it's Fibonacci
    explain_why_fibonacci()
    
    # Visualize for small examples
    visualize_solution(5)
    
    # Trace the optimized solution
    trace_optimized_solution(6)
    
    # Compare approaches
    compare_approaches()
    
    # Test all approaches
    test_all_approaches()
    
    print("=" * 50)
    print("🎓 SUMMARY")
    print("=" * 50)
    print()
    print("✅ OPTIMAL SOLUTION:")
    print("   Use the O(n) time, O(1) space approach")
    print("   with two variables (prev1, prev2)")
    print()
    print("💡 KEY INSIGHT:")
    print("   ways(n) = ways(n-1) + ways(n-2)")
    print("   This is the Fibonacci sequence!")
    print()
    print("📊 COMPLEXITY:")
    print("   Time: O(n)")
    print("   Space: O(1)")
    print()
