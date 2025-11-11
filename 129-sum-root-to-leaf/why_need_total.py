"""
Why We Need total_sum: A Visual Demonstration
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


print("=" * 70)
print("WHY WE NEED total_sum - Visual Explanation")
print("=" * 70)

# Build test tree:   1
#                   / \
#                  2   3
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print("\nTree structure:")
print("   1")
print("  / \\")
print(" 2   3")
print("\nExpected: 12 + 13 = 25\n")


# =============================================================================
# WRONG APPROACH: Trying to reuse current_number
# =============================================================================

def wrong_approach(root):
    """This DOES NOT work - trying to reuse current_number"""
    if not root:
        return 0
    
    print("WRONG APPROACH - Trying to reuse current_number:")
    current_number = 0  # Only ONE variable
    stack = [(root, 0)]
    
    while stack:
        node, num = stack.pop()
        num = num * 10 + node.val
        print(f"  Popped node {node.val}, built number: {num}")
        
        if not node.left and not node.right:
            # Try to accumulate into same variable
            current_number += num
            print(f"    → Leaf! current_number is now: {current_number}")
        
        if node.right:
            stack.append((node.right, num))
        if node.left:
            stack.append((node.left, num))
    
    print(f"  Final result: {current_number}")
    return current_number


# =============================================================================
# CORRECT APPROACH: Separate variables
# =============================================================================

def correct_approach(root):
    """This WORKS - separate current_number and total_sum"""
    if not root:
        return 0
    
    print("\nCORRECT APPROACH - Separate current_number and total_sum:")
    total_sum = 0      # Sum of ALL paths
    stack = [(root, 0)]
    
    while stack:
        node, current_number = stack.pop()
        current_number = current_number * 10 + node.val
        print(f"  Popped node {node.val}, current_number: {current_number}")
        
        if not node.left and not node.right:
            total_sum += current_number
            print(f"    → Leaf! Added {current_number} to total_sum")
            print(f"    → total_sum is now: {total_sum}")
        
        if node.right:
            stack.append((node.right, current_number))
        if node.left:
            stack.append((node.left, current_number))
    
    print(f"  Final result: {total_sum}")
    return total_sum


# Run both
wrong_result = wrong_approach(root)
correct_result = correct_approach(root)

print("\n" + "=" * 70)
print("RESULTS:")
print(f"  Wrong approach:   {wrong_result}")
print(f"  Correct approach: {correct_result}")
print(f"  Expected:         25")
print("=" * 70)


# =============================================================================
# THE CONCEPTUAL DIFFERENCE
# =============================================================================

print("\n" + "=" * 70)
print("CONCEPTUAL EXPLANATION")
print("=" * 70)

print("""
Think of it like this:

╔═══════════════════════════════════════════════════════════════╗
║  current_number = What number am I building RIGHT NOW?        ║
║                   (Changes as I go down EACH path)            ║
║                                                                ║
║  total_sum      = What's the sum of ALL paths I've completed? ║
║                   (Accumulates across ALL paths)              ║
╚═══════════════════════════════════════════════════════════════╝

Stack execution for tree (1, 2, 3):

Step 1: Pop (node=1, current_number=0)
        Build: 0 * 10 + 1 = 1
        current_number = 1
        total_sum = 0  ← hasn't found a leaf yet
        
Step 2: Pop (node=2, current_number=1)
        Build: 1 * 10 + 2 = 12
        current_number = 12  ← THIS path's number
        total_sum = 0
        Leaf! → total_sum = 0 + 12 = 12  ✓
        
Step 3: Pop (node=3, current_number=1)
        Build: 1 * 10 + 3 = 13
        current_number = 13  ← DIFFERENT path's number
        total_sum = 12       ← kept from previous path
        Leaf! → total_sum = 12 + 13 = 25  ✓


KEY INSIGHT:
───────────
Each path has its own current_number!
We can't reuse one variable because:

  Path 1: root(1) → left(2)  builds 12
  Path 2: root(1) → right(3) builds 13
          ↑
          Same starting point, but DIFFERENT numbers!

We need total_sum to ACCUMULATE across all paths.
""")


# =============================================================================
# ANALOGY
# =============================================================================

print("\n" + "=" * 70)
print("ANALOGY: Walking Through a Building")
print("=" * 70)

print("""
Imagine you're in a building with multiple rooms:

🏠 Building (Tree):
   ┌─────┐
   │  1  │  ← Entrance
   └──┬──┘
      │
   ┌──┴──┐
   │     │
┌──▼─┐ ┌─▼──┐
│ 2  │ │ 3  │  ← Two exit doors
└────┘ └────┘

Task: Find the sum of all door numbers from entrance to each exit.

current_number = Which doors have I passed through on THIS path?
                 (e.g., "entered door 1, then door 2" = 12)

total_sum      = Sum of all complete paths' numbers
                 (e.g., path through 1→2 is 12, 
                        path through 1→3 is 13,
                        total = 25)

You CANNOT use one variable because:
- When you're walking path 1→2, you haven't walked 1→3 yet!
- You need to remember the sum from previous completed paths
- Each path is independent until you accumulate them
""")


# =============================================================================
# THE STACK VERSION vs RECURSIVE VERSION
# =============================================================================

print("\n" + "=" * 70)
print("WHY RECURSION DOESN'T NEED total_sum")
print("=" * 70)

print("""
You might notice: The recursive version doesn't have total_sum!

def dfs(node, current_number):
    if not node:
        return 0
    current_number = current_number * 10 + node.val
    if not node.left and not node.right:
        return current_number
    return dfs(node.left, current_number) + dfs(node.right, current_number)
                                            ↑
                                    The + does the accumulation!

The recursive version DOES accumulate, but it's hidden in:
    return left_sum + right_sum

The return values bubble up and get added:
    dfs(1) returns dfs(2) + dfs(3)
                   ↓         ↓
                   12   +    13    = 25

In the stack version, we can't "return and add" because we're not
using function calls. So we need total_sum to manually accumulate.

┌──────────────────────┬─────────────────────────┐
│     RECURSION        │        STACK            │
├──────────────────────┼─────────────────────────┤
│ Accumulation happens │ Must manually track     │
│ through return       │ with total_sum variable │
│ statements           │                         │
└──────────────────────┴─────────────────────────┘
""")


# =============================================================================
# FINAL PROOF
# =============================================================================

print("\n" + "=" * 70)
print("FINAL DEMONSTRATION: Larger Tree")
print("=" * 70)

# Tree:     4
#          / \
#         9   0
#        / \
#       5   1

root2 = TreeNode(4)
root2.left = TreeNode(9)
root2.right = TreeNode(0)
root2.left.left = TreeNode(5)
root2.left.right = TreeNode(1)

print("""
Tree:     4
         / \\
        9   0
       / \\
      5   1

Paths:
  4 → 9 → 5 = 495
  4 → 9 → 1 = 491
  4 → 0     = 40
  Total     = 1026
""")

result = correct_approach(root2)
print(f"\nResult: {result}")
print(f"Expected: 1026")
print(f"Correct: {result == 1026} ✓")

print("\n" + "=" * 70)
print("CONCLUSION")
print("=" * 70)
print("""
✅ YES, you absolutely need total_sum!

Why?
  • current_number tracks ONE path at a time
  • total_sum accumulates ACROSS all paths
  • They serve different purposes
  • You can't reuse one variable for both jobs

Remember:
  current_number = "What number am I building now?"
  total_sum      = "What's my answer so far?"
  
Both are essential! 🎯
""")
