import heapq

nums1 = [5, 3, 8, 1, 2, 7]
nums2 = [3, 1, 4,]

nums_list = nums1 + nums2

max_heap = [ -num for num in nums_list ]  # Negate to simulate max-heap

print("Overall list before heapify:", max_heap)
print("Return value of heapify():", heapq.heapify(max_heap))  # This returns None!

print("Overall list AFTER heapify:", max_heap)  # The list itself is modified!

# Correct way to use heapify:
print("\n" + "="*50)
print("CORRECT USAGE:")

# Method 1: Use the same list variable
my_list = [-5, -3, -8, -1, -2, -7, -3, -1, -4]
print("Before heapify:", my_list)
heapq.heapify(my_list)  # Don't assign the return value!
print("After heapify:", my_list)

# Method 2: Show it's a proper min heap (which acts as max heap due to negation)
print("\nTesting heap property:")
while my_list:
    max_value = -heapq.heappop(my_list)  # Negate back to get original value
    print(f"Popped max value: {max_value}, remaining heap: {my_list}")

##### Heapify from scratch - DEBUGGING THE BUGGY VERSION

print("\n" + "="*60)
print("🐛 ANALYZING THE BUGGY HEAPIFY IMPLEMENTATION")
print("="*60)

def heapify_max_heap_buggy(my_array):
    """BUGGY VERSION - let's see what's wrong"""
    n = len(my_array)
    print(f"Input array: {my_array}")
    
    def heapify_down(arr, n, i):
        print(f"  heapify_down called with i={i}")
        largest_idx = i
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n and arr[left_idx] > arr[largest_idx]:
            largest_idx = left_idx
        if right_idx < n and arr[right_idx] > arr[largest_idx]:
            largest_idx = right_idx
        if largest_idx != i:
            print(f"    Swapping arr[{i}]={arr[i]} with arr[{largest_idx}]={arr[largest_idx]}")
            arr[i], arr[largest_idx] = arr[largest_idx], arr[i]
            heapify_max_heap_buggy(arr)  # BUG 1: Wrong recursive call!
    
    # BUG 2: Never actually calls heapify_down!
    return my_array

print("Testing buggy version:")
my_max_heap_buggy = heapify_max_heap_buggy([3, 5, 20, 10])
print(f"Buggy result: {my_max_heap_buggy}")

print("\n" + "="*60)
print("✅ CORRECT HEAPIFY IMPLEMENTATION")
print("="*60)

def heapify_max_heap_correct(my_array):
    """CORRECT VERSION"""
    n = len(my_array)
    print(f"Input array: {my_array}")
    
    def heapify_down(arr, n, i):
        print(f"  heapify_down called with i={i}")
        largest_idx = i
        left_idx = 2 * i + 1
        right_idx = 2 * i + 2

        if left_idx < n and arr[left_idx] > arr[largest_idx]:
            largest_idx = left_idx
            print(f"    Left child arr[{left_idx}]={arr[left_idx]} > parent")
        if right_idx < n and arr[right_idx] > arr[largest_idx]:
            largest_idx = right_idx
            print(f"    Right child arr[{right_idx}]={arr[right_idx]} > current largest")
            
        if largest_idx != i:
            print(f"    Swapping arr[{i}]={arr[i]} with arr[{largest_idx}]={arr[largest_idx]}")
            arr[i], arr[largest_idx] = arr[largest_idx], arr[i]
            print(f"    Array after swap: {arr}")
            heapify_down(arr, n, largest_idx)  # FIX: Recursive call to heapify_down
    
    # FIX: Actually call heapify_down starting from last non-leaf node
    for i in range(n // 2 - 1, -1, -1):
        print(f"Heapifying from index {i}")
        heapify_down(my_array, n, i)
    
    return my_array

print("Testing correct version:")
my_max_heap_correct = heapify_max_heap_correct([3, 5, 20, 10])
print(f"Correct result: {my_max_heap_correct}")

print("\n" + "="*60)
print("🔍 BUGS IN YOUR ORIGINAL CODE:")
print("="*60)
print("BUG 1: heapify_max_heap(arr) instead of heapify_down(arr, n, largest_idx)")
print("BUG 2: Never actually calls heapify_down - function just returns input!")
print("BUG 3: Should start from last non-leaf node: range(n//2-1, -1, -1)")

print("\n" + "="*60)
print("🧪 VERIFICATION: Testing heap property")
print("="*60)

def verify_max_heap(arr):
    """Verify if array satisfies max heap property"""
    n = len(arr)
    for i in range(n):
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[i] < arr[left]:
            return False, f"Parent arr[{i}]={arr[i]} < left child arr[{left}]={arr[left]}"
        if right < n and arr[i] < arr[right]:
            return False, f"Parent arr[{i}]={arr[i]} < right child arr[{right}]={arr[right]}"
    return True, "Valid max heap!"

is_valid, message = verify_max_heap(my_max_heap_correct)
print(f"Heap verification: {message}")

# Show tree structure
print(f"\nTree structure of {my_max_heap_correct}:")
print(f"       {my_max_heap_correct[0] if len(my_max_heap_correct) > 0 else 'Empty'}")
if len(my_max_heap_correct) > 1:
    print(f"      /   \\")
    print(f"   {my_max_heap_correct[1] if len(my_max_heap_correct) > 1 else 'X'}     {my_max_heap_correct[2] if len(my_max_heap_correct) > 2 else 'X'}")
if len(my_max_heap_correct) > 3:
    print(f"  /")
    print(f"{my_max_heap_correct[3] if len(my_max_heap_correct) > 3 else 'X'}")

print("\n" + "="*60)
print("🤔 WHY IS n // 2 - 1 THE LAST NON-LEAF NODE?")
print("="*60)

def explain_last_nonleaf_formula():
    """Detailed explanation of why n // 2 - 1 is the last non-leaf node"""
    
    print("🔍 MATHEMATICAL PROOF:")
    print("For any node at index i in a 0-based array:")
    print("• Left child is at index: 2*i + 1")
    print("• Right child is at index: 2*i + 2")
    print()
    
    print("A node is a LEAF if it has NO children")
    print("A node is NON-LEAF if it has at least one child")
    print()
    
    # Test with different array sizes
    test_sizes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    for n in test_sizes:
        print(f"📊 Array size n = {n}:")
        print(f"   Indices: {list(range(n))}")
        
        # Calculate last non-leaf using formula
        last_nonleaf = n // 2 - 1
        
        # Verify by checking each node
        leaf_nodes = []
        nonleaf_nodes = []
        
        for i in range(n):
            left_child = 2 * i + 1
            right_child = 2 * i + 2
            
            has_left = left_child < n
            has_right = right_child < n
            
            if has_left or has_right:
                nonleaf_nodes.append(i)
            else:
                leaf_nodes.append(i)
        
        actual_last_nonleaf = nonleaf_nodes[-1] if nonleaf_nodes else -1
        
        print(f"   Formula result: n//2-1 = {n}//2-1 = {last_nonleaf}")
        print(f"   Non-leaf nodes: {nonleaf_nodes}")
        print(f"   Leaf nodes: {leaf_nodes}")
        print(f"   Actual last non-leaf: {actual_last_nonleaf}")
        print(f"   Formula correct? {last_nonleaf == actual_last_nonleaf} ✅" if last_nonleaf == actual_last_nonleaf else f"   Formula correct? ❌")
        
        # Show tree structure for smaller arrays
        if n <= 7:
            print("   Tree structure:")
            if n >= 1:
                print(f"           0")
            if n >= 2:
                print(f"          / \\")
                print(f"         1   {2 if n > 2 else 'X'}")
            if n >= 4:
                print(f"        / \\ / \\")
                print(f"       3  {4 if n > 4 else 'X'} {5 if n > 5 else 'X'}  {6 if n > 6 else 'X'}")
        print()

explain_last_nonleaf_formula()

print("🧮 MATHEMATICAL DERIVATION:")
print("="*50)
print("For a node at index i to be a NON-LEAF:")
print("• It must have at least one child")
print("• Left child: 2*i + 1 < n")
print("• This means: i < (n-1)/2")
print("• The largest integer i satisfying this is: floor((n-1)/2)")
print("• Which equals: (n-1)//2")
print("• But wait! Let's be more careful...")
print()
print("For the LAST node that has children:")
print("• We want the largest i such that 2*i + 1 < n")
print("• Rearranging: i < (n-1)/2")
print("• Largest integer i: floor((n-1)/2) = (n-1)//2")
print()
print("But there's a simpler way to think about it:")
print("• In a complete binary tree with n nodes")
print("• The first n//2 nodes (indices 0 to n//2-1) have children")
print("• The last n//2 nodes (indices n//2 to n-1) are leaves")
print("• So the last non-leaf is at index n//2 - 1")

print("\n✅ KEY INSIGHT:")
print("The formula n//2 - 1 works because:")
print("• First half of array: internal nodes (have children)")
print("• Second half of array: leaf nodes (no children)")
print("• The boundary is exactly at index n//2")
print("• So last non-leaf is at index n//2 - 1")

print("\n" + "="*60)
print("🤔 WHY START FROM LAST NON-LEAF NODE, NOT LEAF NODE?")
print("="*60)

def demonstrate_heapify_strategy():
    """Show why we start from non-leaf nodes, not leaf nodes"""
    
    print("🔍 THE FUNDAMENTAL INSIGHT:")
    print("• LEAF NODES are already valid heaps by themselves!")
    print("• NON-LEAF NODES might violate heap property")
    print("• We need to 'fix' non-leaf nodes by heapifying down")
    print()
    
    # Example array that violates heap property
    broken_heap = [1, 10, 5, 20, 15]
    print(f"Example broken heap: {broken_heap}")
    print("Tree structure:")
    print("       1")
    print("      / \\")
    print("    10   5")
    print("   /  \\")
    print("  20  15")
    print()
    
    n = len(broken_heap)
    last_nonleaf = n // 2 - 1
    
    print(f"n = {n}, last non-leaf = n//2-1 = {last_nonleaf}")
    print(f"Non-leaf nodes: indices {list(range(last_nonleaf + 1))} = {[broken_heap[i] for i in range(last_nonleaf + 1)]}")
    print(f"Leaf nodes: indices {list(range(last_nonleaf + 1, n))} = {[broken_heap[i] for i in range(last_nonleaf + 1, n)]}")
    print()
    
    print("💡 WHY LEAF NODES DON'T NEED HEAPIFYING:")
    print("• A leaf node has NO children")
    print("• Heap property: parent ≥ children (for max heap)")
    print("• If there are no children, heap property is AUTOMATICALLY satisfied!")
    print("• Leaf nodes are already 'mini-heaps' of size 1")
    print()
    
    print("🔧 WHY NON-LEAF NODES NEED HEAPIFYING:")
    print("• Non-leaf nodes HAVE children")
    print("• They might violate: parent ≥ children")
    print("• We need to 'bubble down' to fix violations")
    print("• Must work BOTTOM-UP to ensure correctness")
    print()
    
    print("🧪 SIMULATION: What happens if we 'heapify' leaf nodes?")
    print("="*55)
    
    def try_heapify_leaf(arr, i):
        print(f"  Trying to heapify leaf node at index {i} (value {arr[i]}):")
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left >= len(arr) and right >= len(arr):
            print(f"    No children - nothing to do! Already a valid heap.")
            return False
        else:
            print(f"    This shouldn't happen for a leaf node!")
            return True
    
    # Try heapifying leaf nodes
    for i in range(last_nonleaf + 1, n):
        try_heapify_leaf(broken_heap, i)
    
    print("\n🎯 BOTTOM-UP STRATEGY:")
    print("="*30)
    print("1. Start from LAST NON-LEAF node (deepest level)")
    print("2. Heapify each non-leaf node going UPWARD")
    print("3. This ensures lower levels are fixed before upper levels")
    print("4. By the time we reach root, entire tree is heapified")
    print()
    
    # Show correct heapification
    print("✅ CORRECT HEAPIFICATION (bottom-up from non-leaf nodes):")
    test_arr = broken_heap.copy()
    
    def simple_heapify_down(arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
            
        if largest != i:
            print(f"    Index {i}: Swap {arr[i]} ↔ {arr[largest]}")
            arr[i], arr[largest] = arr[largest], arr[i]
            print(f"    Array: {arr}")
            # Recursively heapify affected subtree
            simple_heapify_down(arr, n, largest)
        else:
            print(f"    Index {i}: No swap needed - heap property satisfied")
    
    for i in range(last_nonleaf, -1, -1):
        print(f"  Heapifying non-leaf node {i} (value {test_arr[i]}):")
        simple_heapify_down(test_arr, n, i)
    
    print(f"\n🎉 Final result: {test_arr}")
    print("Tree structure after heapification:")
    print(f"      {test_arr[0]}")
    print(f"     / \\")
    print(f"   {test_arr[1]}   {test_arr[2]}")
    print(f"  / \\")
    print(f" {test_arr[3]} {test_arr[4]}")

demonstrate_heapify_strategy()

print("\n" + "="*60)
print("📚 SUMMARY: Why Start from Non-Leaf Nodes")
print("="*60)
print("1. 🍃 LEAF NODES: Already satisfy heap property (no children to compare)")
print("2. 🌿 NON-LEAF NODES: May violate heap property (need fixing)")
print("3. ⬇️  HEAPIFY DOWN: Process of fixing violations by moving down")
print("4. 📍 BOTTOM-UP: Start from deepest non-leaf, work toward root")
print("5. ✅ EFFICIENCY: Skip leaf nodes (already valid), focus on problem nodes")
print("6. 🎯 CORRECTNESS: Ensures lower levels fixed before upper levels")
print("\nStarting from leaf nodes would be:")
print("❌ Inefficient (wasted work on nodes that don't need fixing)")
print("❌ Incorrect (wouldn't properly fix the heap structure)")
print("✅ Starting from non-leaf nodes is the ONLY correct approach!")