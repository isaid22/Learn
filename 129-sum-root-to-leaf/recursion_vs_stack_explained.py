"""
RECURSION vs STACK - A Complete Guide
======================================

This file explains how stack can replace recursion with detailed examples.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# =============================================================================
# EXAMPLE 1: Simple Tree Traversal (Easier to understand)
# =============================================================================

print("=" * 70)
print("EXAMPLE 1: Pre-order Traversal (Root -> Left -> Right)")
print("=" * 70)

def preorder_recursive(node, result=None):
    """Recursive approach"""
    if result is None:
        result = []
    
    if not node:
        return result
    
    # Process current node
    result.append(node.val)
    # Recurse on left
    preorder_recursive(node.left, result)
    # Recurse on right
    preorder_recursive(node.right, result)
    
    return result


def preorder_stack(root):
    """Stack approach - doing the SAME thing manually"""
    if not root:
        return []
    
    result = []
    stack = [root]  # Start with root in stack
    
    while stack:
        # Pop = "visiting" this node (like entering a recursive call)
        node = stack.pop()
        
        # Process current node
        result.append(node.val)
        
        # Add children to stack (RIGHT first, then LEFT)
        # Why? Stack is LIFO (Last In First Out)
        # We want left to be processed first, so add it last
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# Test Example 1
#     1
#    / \
#   2   3
#  / \
# 4   5
tree1 = TreeNode(1)
tree1.left = TreeNode(2)
tree1.right = TreeNode(3)
tree1.left.left = TreeNode(4)
tree1.left.right = TreeNode(5)

print("\nTree structure:")
print("     1")
print("    / \\")
print("   2   3")
print("  / \\")
print(" 4   5")
print()

rec_result = preorder_recursive(tree1)
stack_result = preorder_stack(tree1)

print(f"Recursive result: {rec_result}")
print(f"Stack result:     {stack_result}")
print(f"Same? {rec_result == stack_result} ✓")


# =============================================================================
# EXAMPLE 2: Our LeetCode Problem - Step by Step
# =============================================================================

print("\n" + "=" * 70)
print("EXAMPLE 2: Sum Root to Leaf Numbers (Our Problem)")
print("=" * 70)

def sum_numbers_recursive(root):
    """RECURSIVE: What's happening at each step"""
    def dfs(node, current_num):
        print(f"  → Entering: node={node.val if node else None}, current_num={current_num}")
        
        if not node:
            print(f"    ← Returning: 0 (null node)")
            return 0
        
        # Build number
        current_num = current_num * 10 + node.val
        print(f"    Built number: {current_num}")
        
        # Leaf node?
        if not node.left and not node.right:
            print(f"    ← Leaf! Returning: {current_num}")
            return current_num
        
        # Recurse
        left_sum = dfs(node.left, current_num)
        right_sum = dfs(node.right, current_num)
        
        total = left_sum + right_sum
        print(f"    ← Returning: {left_sum} + {right_sum} = {total}")
        return total
    
    print("\nRECURSIVE EXECUTION:")
    return dfs(root, 0)


def sum_numbers_stack(root):
    """STACK: Doing the SAME thing manually"""
    if not root:
        return 0
    
    print("\nSTACK EXECUTION:")
    total_sum = 0
    stack = [(root, 0)]  # (node, number_built_so_far)
    
    while stack:
        node, current_num = stack.pop()
        print(f"  → Popped: node={node.val}, current_num={current_num}")
        
        # Build number (same logic as recursive)
        current_num = current_num * 10 + node.val
        print(f"    Built number: {current_num}")
        
        # Leaf node?
        if not node.left and not node.right:
            print(f"    Leaf! Adding {current_num} to total")
            total_sum += current_num
        
        # Add children to stack (instead of recursing)
        if node.right:
            print(f"    Pushing right child: {node.right.val}")
            stack.append((node.right, current_num))
        if node.left:
            print(f"    Pushing left child: {node.left.val}")
            stack.append((node.left, current_num))
    
    print(f"  Final total: {total_sum}")
    return total_sum


# Test with simple tree
#   1
#  / \
# 2   3
print("\nTree structure:")
print("   1")
print("  / \\")
print(" 2   3")
print("Expected: 12 + 13 = 25\n")

tree2 = TreeNode(1)
tree2.left = TreeNode(2)
tree2.right = TreeNode(3)

rec_result = sum_numbers_recursive(tree2)
stack_result = sum_numbers_stack(tree2)

print(f"\nRecursive final answer: {rec_result}")
print(f"Stack final answer:     {stack_result}")
print(f"Same? {rec_result == stack_result} ✓")


# =============================================================================
# KEY INSIGHTS - How to Convert Recursion to Stack
# =============================================================================

print("\n" + "=" * 70)
print("HOW TO CONVERT RECURSION TO STACK")
print("=" * 70)

print("""
STEP-BY-STEP PATTERN:

1. IDENTIFY what you need to remember for each "call"
   Recursive: function parameters
   Stack:     tuple/object with same data
   
2. CREATE the stack and push initial state
   Recursive: call function with root
   Stack:     push (root, initial_params) to stack
   
3. LOOP while stack is not empty
   Recursive: base case stops recursion
   Stack:     empty stack stops loop
   
4. POP from stack (= "entering" a recursive call)
   Recursive: function gets called with parameters
   Stack:     pop() gives you the same data
   
5. PROCESS current node
   Both do the same work!
   
6. PUSH children to stack (= "making" recursive calls)
   Recursive: call function(child)
   Stack:     stack.append((child, params))


VISUALIZATION:

Recursive Call Stack (automatic):     Explicit Stack (manual):
┌─────────────────────┐                ┌─────────────────────┐
│ dfs(node=3, num=1)  │                │ (node=3, num=1)     │
├─────────────────────┤                ├─────────────────────┤
│ dfs(node=2, num=1)  │                │ (node=2, num=1)     │
├─────────────────────┤                ├─────────────────────┤
│ dfs(node=1, num=0)  │                │ (node=1, num=0)     │
└─────────────────────┘                └─────────────────────┘
      (grows down)                          (grows up)
      
Both contain THE SAME INFORMATION!


WHEN TO USE EACH:

✓ Use RECURSION when:
  - Code clarity is important
  - Tree depth is reasonable (< 1000 levels)
  - You want clean, elegant code

✓ Use STACK when:
  - Tree might be very deep (avoid stack overflow)
  - You need more control over execution order
  - Converting existing recursive code that has issues


COMMON PATTERNS:

Pattern 1: DFS (Depth-First Search)
- Use stack (LIFO = Last In First Out)
- Explores deep before wide

Pattern 2: BFS (Breadth-First Search)  
- Use queue (FIFO = First In First Out)
- Explores wide before deep
- CANNOT be done with simple recursion!

""")


# =============================================================================
# PRACTICE: Try converting this recursive function to stack!
# =============================================================================

print("=" * 70)
print("PRACTICE PROBLEM")
print("=" * 70)

def max_depth_recursive(root):
    """Find maximum depth of binary tree - RECURSIVE"""
    if not root:
        return 0
    
    left_depth = max_depth_recursive(root.left)
    right_depth = max_depth_recursive(root.right)
    
    return 1 + max(left_depth, right_depth)


def max_depth_stack(root):
    """Find maximum depth of binary tree - STACK VERSION"""
    if not root:
        return 0
    
    max_depth = 0
    # Stack contains: (node, depth_at_this_node)
    stack = [(root, 1)]
    
    while stack:
        node, depth = stack.pop()
        
        # Update max depth
        max_depth = max(max_depth, depth)
        
        # Add children with incremented depth
        if node.right:
            stack.append((node.right, depth + 1))
        if node.left:
            stack.append((node.left, depth + 1))
    
    return max_depth


# Test
print("\nFinding max depth of tree:")
print("     1")
print("    / \\")
print("   2   3")
print("  / \\")
print(" 4   5")
print()

rec_depth = max_depth_recursive(tree1)
stack_depth = max_depth_stack(tree1)

print(f"Recursive max depth: {rec_depth}")
print(f"Stack max depth:     {stack_depth}")
print(f"Same? {rec_depth == stack_depth} ✓")


print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)
print("""
🔑 KEY TAKEAWAY: 
Stack is not just a substitute for recursion - it IS recursion, 
just with the call stack made explicit!

When you understand this, you can:
1. Convert any recursive algorithm to iterative
2. Avoid stack overflow for deep trees
3. Have more control over execution
4. Debug more easily (you can see the stack!)

Practice by converting recursive solutions to stack-based ones.
After a few tries, the pattern will become second nature! 💪
""")
