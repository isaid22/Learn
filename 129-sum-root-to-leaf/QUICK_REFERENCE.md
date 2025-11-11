# Recursion ↔ Stack Quick Reference Guide

## The Core Concept

**Recursion and Stack are THE SAME THING!**

- **Recursion**: Computer manages the stack automatically (call stack)
- **Stack**: You manage the stack manually (explicit stack)

---

## When to Use Which?

### ✅ Use Recursion When:
- Code clarity matters most
- Tree depth < 1000 (no stack overflow risk)
- You want concise, elegant code
- Problem naturally fits recursive thinking

### ✅ Use Stack When:
- Tree might be very deep (avoid stack overflow)
- You need to see/debug what's in the "call stack"
- Converting problematic recursive code
- You find it easier to think iteratively

---

## The Conversion Pattern

### Step 1: Identify What to Remember
```python
# Recursion: function parameters
def dfs(node, current_sum, depth):
    ...

# Stack: tuple with same data
stack = [(node, current_sum, depth)]
```

### Step 2: Base Case → Empty Stack
```python
# Recursion
if not node:
    return default_value

# Stack
while stack:  # Stops when empty
    node, data = stack.pop()
```

### Step 3: Recursive Call → Stack Push
```python
# Recursion
result = dfs(node.left, new_param)

# Stack
stack.append((node.left, new_param))
```

### Step 4: Return → Accumulate
```python
# Recursion
return left_result + right_result

# Stack
total += current_result  # Accumulate as you go
```

---

## Side-by-Side Template

```python
# ============== RECURSION ==============
def solve(root):
    def helper(node, param):
        if not node:
            return 0
        
        # Process
        value = node.val + param
        
        # Leaf?
        if not node.left and not node.right:
            return value
        
        # Recurse
        left = helper(node.left, value)
        right = helper(node.right, value)
        
        return left + right
    
    return helper(root, 0)


# ============== STACK ==================
def solve(root):
    if not root:
        return 0
    
    total = 0
    stack = [(root, 0)]
    
    while stack:
        node, param = stack.pop()
        
        # Process (SAME!)
        value = node.val + param
        
        # Leaf? (SAME!)
        if not node.left and not node.right:
            total += value
            continue
        
        # Add children
        if node.right:
            stack.append((node.right, value))
        if node.left:
            stack.append((node.left, value))
    
    return total
```

---

## Common Mistakes to Avoid

### ❌ Mistake 1: Wrong Order in Stack
```python
# Wrong - processes in wrong order
if node.left:
    stack.append(node.left)
if node.right:
    stack.append(node.right)

# Right - push right first (for DFS left-to-right)
if node.right:
    stack.append(node.right)
if node.left:
    stack.append(node.left)
```

### ❌ Mistake 2: Forgetting to Update Parameters
```python
# Wrong - uses old value
stack.append((node.left, current_sum))

# Right - pass updated value
new_sum = current_sum + node.val
stack.append((node.left, new_sum))
```

### ❌ Mistake 3: Not Handling Null
```python
# Wrong - will crash
stack.append((node.left, value))

# Right - check first
if node.left:
    stack.append((node.left, value))
```

---

## Memory Aid: The 5 Questions

When converting, ask yourself:

1. **What to remember?** → Look at function parameters
2. **When to stop?** → Base case → Empty stack
3. **What to do?** → Process logic (same for both!)
4. **How to explore?** → Recursive call → Stack push
5. **How to combine?** → Return → Accumulate

---

## Practice Problems (Easy → Hard)

### Level 1: Tree Traversal
- Preorder traversal
- Inorder traversal  
- Postorder traversal

### Level 2: Single Path
- Maximum depth
- Minimum depth
- Path sum
- **Sum root to leaf (our problem!)**

### Level 3: Multiple Paths
- All paths from root to leaf
- Path sum II (all paths with target)
- Binary tree paths

### Level 4: Complex Logic
- Lowest common ancestor
- Validate BST
- Serialize/deserialize tree

---

## Quick Reference: DFS vs BFS

```python
# DFS (Depth-First) - Use STACK
stack = [root]
while stack:
    node = stack.pop()  # LIFO - Last In First Out
    # Process node
    if node.right: stack.append(node.right)
    if node.left: stack.append(node.left)

# BFS (Breadth-First) - Use QUEUE
from collections import deque
queue = deque([root])
while queue:
    node = queue.popleft()  # FIFO - First In First Out
    # Process node
    if node.left: queue.append(node.left)
    if node.right: queue.append(node.right)
```

---

## The "Aha!" Moment

> **When you write `dfs(node.left)`, the computer pushes to its hidden stack.**
> 
> **When you write `stack.append(node.left)`, you push to your visible stack.**
> 
> **SAME THING, DIFFERENT VISIBILITY!** 💡

---

## Final Tips

1. **Start with Stack** if recursion confuses you - it's more explicit
2. **Draw small examples** - trace both approaches on paper
3. **Print the stack** - see what's happening at each step
4. **Trust the pattern** - after 5-10 conversions, it becomes automatic
5. **Both are valid** - choose based on clarity and constraints

---

## Files in This Folder

- `makesum.py` - The LeetCode solution (both recursive and iterative)
- `recursion_vs_stack_explained.py` - Detailed examples with execution traces
- `understanding_recursion.py` - Mental models and thinking patterns
- `QUICK_REFERENCE.md` - This file!

---

**Remember:** You're not choosing between recursion and stack - you're choosing between **automatic** and **manual** stack management. The algorithm is the same! 🚀
