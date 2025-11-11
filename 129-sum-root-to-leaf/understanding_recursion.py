"""
The Mental Model: How to Think About Recursion vs Stack
========================================================

This guide helps you develop intuition for converting between approaches.
"""

# =============================================================================
# THE FUNDAMENTAL INSIGHT
# =============================================================================

print("=" * 70)
print("THE FUNDAMENTAL INSIGHT")
print("=" * 70)
print("""
When you write:
    dfs(node.left)
    
The computer does this:
    1. Saves current state (where to return, all variables)
    2. Jumps to execute dfs with new parameters
    3. When done, restores state and continues
    
When you write:
    stack.append(node.left)
    
YOU are doing step 1 manually!
Then the while loop does steps 2-3.

IT'S THE SAME THING! 🤯
""")


# =============================================================================
# THINKING PATTERN: Question to Ask Yourself
# =============================================================================

print("=" * 70)
print("THE THINKING PATTERN")
print("=" * 70)
print("""
When converting recursion → stack, ask these questions:

┌─────────────────────────────────────────────────────────────┐
│ Question 1: What do I need to "remember" for each node?     │
└─────────────────────────────────────────────────────────────┘
   
   Recursion: Look at function parameters
   Example: def dfs(node, current_number):
            ↓
   Stack:   Store tuple with same data
   Example: stack = [(node, current_number)]


┌─────────────────────────────────────────────────────────────┐
│ Question 2: When do I stop?                                  │
└─────────────────────────────────────────────────────────────┘
   
   Recursion: Base case (if not node: return)
   Stack:     Empty stack (while stack:)


┌─────────────────────────────────────────────────────────────┐
│ Question 3: What do I do at each step?                       │
└─────────────────────────────────────────────────────────────┘
   
   Both: EXACTLY the same logic!
   Just access data differently:
   - Recursion: from parameters
   - Stack:     from popped tuple


┌─────────────────────────────────────────────────────────────┐
│ Question 4: How do I explore children?                       │
└─────────────────────────────────────────────────────────────┘
   
   Recursion: Call function recursively
   Example: dfs(node.left, new_num)
            ↓
   Stack:   Push to stack
   Example: stack.append((node.left, new_num))


┌─────────────────────────────────────────────────────────────┐
│ Question 5: How do I combine results from children?          │
└─────────────────────────────────────────────────────────────┘
   
   Recursion: Return value back up
   Example: return left_sum + right_sum
            ↓
   Stack:   Keep running total
   Example: total_sum += current_value
""")


# =============================================================================
# SIDE-BY-SIDE TEMPLATE
# =============================================================================

print("\n" + "=" * 70)
print("SIDE-BY-SIDE TEMPLATE")
print("=" * 70)
print("""
┌──────────────────────────────┬──────────────────────────────┐
│        RECURSION             │          STACK               │
├──────────────────────────────┼──────────────────────────────┤
│ def solve(root):             │ def solve(root):             │
│     def helper(node, param): │     if not root:             │
│         # Base case          │         return default       │
│         if not node:         │                              │
│             return default   │     result = initial         │
│                              │     stack = [(root, param)]  │
│         # Process node       │                              │
│         value = process(     │     while stack:             │
│             node, param)     │         node, param =        │
│                              │             stack.pop()      │
│         # Leaf case          │                              │
│         if is_leaf(node):    │         # Process node       │
│             return value     │         value = process(     │
│                              │             node, param)     │
│         # Recurse            │                              │
│         left = helper(       │         # Leaf case          │
│             node.left,       │         if is_leaf(node):    │
│             new_param)       │             update(result,   │
│         right = helper(      │                    value)    │
│             node.right,      │             continue         │
│             new_param)       │                              │
│                              │         # Add children       │
│         # Combine            │         if node.right:       │
│         return combine(      │             stack.append(    │
│             left, right)     │                 (node.right, │
│                              │                  new_param)) │
│     return helper(root, 0)   │         if node.left:        │
│                              │             stack.append(    │
│                              │                 (node.left,  │
│                              │                  new_param)) │
│                              │                              │
│                              │     return result            │
└──────────────────────────────┴──────────────────────────────┘

Notice: Same logic, different mechanics!
""")


# =============================================================================
# CONCRETE EXAMPLE WITH ANNOTATIONS
# =============================================================================

print("\n" + "=" * 70)
print("ANNOTATED EXAMPLE: Sum Root to Leaf")
print("=" * 70)

print("""
RECURSION VERSION (What the computer does for you):
───────────────────────────────────────────────────

def sumNumbers(root):
    def dfs(node, num):
        if not node:                    ← Stop condition
            return 0
        
        num = num * 10 + node.val       ← Process current
        
        if not node.left and not node.right:  ← Leaf check
            return num
        
        left = dfs(node.left, num)      ← Computer saves state here!
        right = dfs(node.right, num)    ← And here!
        
        return left + right             ← Combine results
    
    return dfs(root, 0)


Behind the scenes, computer maintains call stack:
┌──────────────────┐
│ dfs(node3, 1)    │ ← Most recent call
├──────────────────┤
│ dfs(node2, 1)    │
├──────────────────┤
│ dfs(node1, 0)    │ ← Original call
└──────────────────┘


STACK VERSION (What YOU do manually):
──────────────────────────────────────

def sumNumbers(root):
    if not root:                        ← Stop condition
        return 0
    
    total = 0                           ← Accumulator for results
    stack = [(root, 0)]                 ← YOU create the stack!
    
    while stack:                        ← Instead of recursion
        node, num = stack.pop()         ← YOU pop the state
        
        num = num * 10 + node.val       ← Process current (SAME!)
        
        if not node.left and not node.right:  ← Leaf check (SAME!)
            total += num                ← Accumulate instead of return
            continue
        
        if node.right:                  ← YOU save right child state
            stack.append((node.right, num))
        if node.left:                   ← YOU save left child state
            stack.append((node.left, num))
    
    return total


YOU maintain the stack explicitly:
┌──────────────────┐
│ (node3, 1)       │ ← You pushed this
├──────────────────┤
│ (node2, 1)       │ ← You pushed this
├──────────────────┤
│ (node1, 0)       │ ← You started with this
└──────────────────┘

SAME DATA, SAME LOGIC, JUST EXPLICIT! ✨
""")


# =============================================================================
# PRACTICAL TIPS
# =============================================================================

print("\n" + "=" * 70)
print("PRACTICAL TIPS FOR LEARNING RECURSION")
print("=" * 70)
print("""
1️⃣  DRAW IT OUT
   ────────────
   For small examples, draw the tree and trace execution:
   - Recursion: Draw calls going down, returns going up
   - Stack: Draw what's in the stack at each step
   
   Example tree:  1
                 / \\
                2   3
   
   Trace both approaches on paper!


2️⃣  TRUST THE RECURSION (hardest part!)
   ────────────────────────────────────
   Don't try to trace every recursive call in your head.
   Instead, assume the recursive call works for smaller inputs.
   
   Example:
   "If dfs(left_child) gives me the sum for left subtree,
    and dfs(right_child) gives me the sum for right subtree,
    then I just need to add them!"
   
   This is the LEAP OF FAITH in recursion.


3️⃣  START WITH STACK IF RECURSION IS HARD
   ───────────────────────────────────────
   Stack gives you more visibility:
   - You can print the stack at each step
   - You can see exactly what's being processed
   - No "magic" - everything is explicit
   
   Once comfortable with stack, recursion will make more sense!


4️⃣  PRACTICE THE CONVERSION
   ─────────────────────────
   Take any recursive solution and convert to stack.
   After 5-10 conversions, the pattern becomes automatic.
   
   Good practice problems:
   - Tree traversals (preorder, inorder, postorder)
   - Tree depth/height
   - Path sum problems
   - Validate BST


5️⃣  RECOGNIZE THE PATTERN
   ──────────────────────
   Most tree problems follow this pattern:
   
   1. Process current node
   2. Handle base case (null or leaf)
   3. Explore children
   4. Combine results
   
   Once you see this pattern, both recursion and stack
   become tools to implement the SAME algorithm.
""")


# =============================================================================
# FINAL EXAMPLE: Let's convert a new problem together!
# =============================================================================

print("\n" + "=" * 70)
print("EXERCISE: Convert This Together!")
print("=" * 70)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


print("""
Problem: Find if a path exists from root to leaf with given sum.

Given:       5
           /   \\
          4     8
         /     / \\
        11    13  4
       /  \\        \\
      7    2        1
      
Target sum = 22
Answer: True (5 → 4 → 11 → 2 = 22)
""")


def has_path_sum_recursive(root, target_sum):
    """Recursive version"""
    if not root:
        return False
    
    # If leaf, check if we've reached the target
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recursively check children with reduced sum
    remaining = target_sum - root.val
    return (has_path_sum_recursive(root.left, remaining) or
            has_path_sum_recursive(root.right, remaining))


def has_path_sum_stack(root, target_sum):
    """Stack version - following the pattern!"""
    if not root:
        return False
    
    # Stack stores: (node, remaining_sum_needed)
    stack = [(root, target_sum)]
    
    while stack:
        node, remaining = stack.pop()
        
        # If leaf, check if we've reached the target
        if not node.left and not node.right:
            if node.val == remaining:
                return True
            continue
        
        # Add children with reduced sum
        new_remaining = remaining - node.val
        if node.right:
            stack.append((node.right, new_remaining))
        if node.left:
            stack.append((node.left, new_remaining))
    
    return False


# Build test tree
root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)

print("\nTesting with target_sum = 22:")
print(f"Recursive: {has_path_sum_recursive(root, 22)}")
print(f"Stack:     {has_path_sum_stack(root, 22)}")

print("\nTesting with target_sum = 100:")
print(f"Recursive: {has_path_sum_recursive(root, 100)}")
print(f"Stack:     {has_path_sum_stack(root, 100)}")

print("""
See the pattern?
- Identify what to remember: (node, remaining_sum)
- Process node: check if leaf
- Explore children: push to stack with updated remaining
- Both versions do THE SAME THING! ✓
""")


print("\n" + "=" * 70)
print("FINAL THOUGHTS")
print("=" * 70)
print("""
🎯 Key Insight:
   Recursion is just a fancy way of using a stack.
   Stack is just a manual way of doing recursion.
   They are TWO WAYS TO WRITE THE SAME ALGORITHM.

📚 Learning Path:
   1. Study stack version first (more visible)
   2. Understand what data goes in the stack
   3. See how stack processing matches recursive logic
   4. Practice converting both ways
   5. Eventually, recursion will "click"!

💪 You've got this!
   Keep practicing, and recursion will become intuitive.
   Remember: every recursive solution can be rewritten
   with a stack, so you're never stuck! 🚀
""")
