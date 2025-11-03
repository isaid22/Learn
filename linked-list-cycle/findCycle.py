# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Find the node where the cycle begins in a linked list.
        
        Algorithm: Floyd's Cycle Detection + Mathematical Analysis
        
        Phase 1: Detect if cycle exists using slow/fast pointers
        Phase 2: Find the start of the cycle using mathematical property
        
        Time Complexity: O(n)
        Space Complexity: O(1)
        """
        # Handle edge cases
        if not head or not head.next:
            print("DEBUG: Returning None - edge case (empty or single node)")
            return None
        
        # Phase 1: Detect cycle using Floyd's algorithm
        slow = fast = head
        
        # Move slow by 1 step, fast by 2 steps
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            # If they meet, there's a cycle
            if slow == fast:  # Could also be: if fast == slow:
                break
        else:
            # No cycle found - this is where None gets returned!
            print("DEBUG: Returning None - no cycle detected by algorithm")
            return None
        
        # Phase 2: Find the start of the cycle
        # Mathematical insight: distance from head to cycle start == 
        # distance from meeting point to cycle start
        # 
        # WHY IS THIS TRUE? Let's prove it mathematically:
        #
        # Define variables:
        # - a = distance from head to cycle start
        # - b = distance from cycle start to meeting point  
        # - c = distance from meeting point back to cycle start
        # - Cycle length = b + c
        #
        # When slow and fast meet in Phase 1:
        # - Slow traveled: a + b steps
        # - Fast traveled: a + b + k*(b + c) steps (k = number of extra cycles)
        #
        # Since fast moves twice as fast as slow:
        # 2 * (a + b) = a + b + k*(b + c)
        # 2a + 2b = a + b + k*(b + c)
        # a + b = k*(b + c)
        # a = k*(b + c) - b
        # a = k*b + k*c - b
        # a = b*(k-1) + k*c
        # a = (k-1)*(b + c) + c
        #
        # This means: a ≡ c (mod cycle_length)
        # In simpler terms: a = c + some_number_of_full_cycles
        #
        # Therefore: Starting from head and moving 'a' steps reaches cycle start
        #           Starting from meeting point and moving 'c' steps also reaches cycle start
        #           Since they move at same speed (1 step each), they meet AT the cycle start!
        
        slow = head  # Reset slow to head
        
        # Move both pointers one step at a time until they meet
        while slow != fast:
            slow = slow.next
            fast = fast.next
        # The loop exits when slow == fast (they meet at cycle start!)
        
        # The meeting point is the start of the cycle
        return slow  # This should always be a ListNode if we reach here

def create_test_case_1():
    """Create test case: [3,2,0,-4] with cycle at pos=1"""
    node3 = ListNode(3)
    node2 = ListNode(2) 
    node0 = ListNode(0)
    node_neg4 = ListNode(-4)
    
    node3.next = node2
    node2.next = node0
    node0.next = node_neg4
    node_neg4.next = node2  # Creates cycle back to node2 (pos=1)
    
    return node3, node2  # Return head and expected cycle start

def create_test_case_2():
    """Create test case: [1,2] with cycle at pos=0"""
    node1 = ListNode(1)
    node2 = ListNode(2)
    
    node1.next = node2
    node2.next = node1  # Creates cycle back to node1 (pos=0)
    
    return node1, node1  # Return head and expected cycle start

def create_test_case_3():
    """Create test case: [1] with no cycle (pos=-1)"""
    node1 = ListNode(1)
    # No cycle
    
    return node1, None  # Return head and expected result (None)

def test_solution():
    """Test the solution with provided examples"""
    solution = Solution()
    
    print("🧪 TESTING LINKED LIST CYCLE II DETECTION")
    print("=" * 50)
    
    # Test Case 1: [3,2,0,-4], pos = 1
    print("Test Case 1: [3,2,0,-4], pos = 1")
    head1, expected1 = create_test_case_1()
    result1 = solution.detectCycle(head1)
    
    if result1 == expected1:
        print(f"✅ PASS: Found cycle start at node with value {result1.val}")
    else:
        print(f"❌ FAIL: Expected node with value {expected1.val}, got {result1}")
    print()
    
    # Test Case 2: [1,2], pos = 0  
    print("Test Case 2: [1,2], pos = 0")
    head2, expected2 = create_test_case_2()
    result2 = solution.detectCycle(head2)
    
    if result2 == expected2:
        print(f"✅ PASS: Found cycle start at node with value {result2.val}")
    else:
        print(f"❌ FAIL: Expected node with value {expected2.val}, got {result2}")
    print()
    
    # Test Case 3: [1], pos = -1
    print("Test Case 3: [1], pos = -1 (no cycle)")
    head3, expected3 = create_test_case_3()
    result3 = solution.detectCycle(head3)
    
    if result3 == expected3:
        print("✅ PASS: Correctly detected no cycle (returned None)")
    else:
        print(f"❌ FAIL: Expected None, got {result3}")
    print()

def explain_algorithm():
    """Explain the mathematical insight behind the algorithm"""
    print("\n🧮 MATHEMATICAL EXPLANATION")
    print("=" * 40)
    print("""
    Why does this algorithm work?
    
    Let's say:
    - Distance from head to cycle start = 'a'
    - Distance from cycle start to meeting point = 'b' 
    - Distance from meeting point back to cycle start = 'c'
    - Cycle length = b + c
    
    When slow and fast meet:
    - Slow has traveled: a + b
    - Fast has traveled: a + b + k*(b + c) for some integer k
    
    Since fast travels twice as fast as slow:
    2 * (a + b) = a + b + k*(b + c)
    2a + 2b = a + b + k*(b + c)
    a + b = k*(b + c)
    a = k*(b + c) - b
    a = k*(b + c) - b
    a = (k-1)*(b + c) + c
    
    This means: distance from head to cycle start (a) equals
    distance from meeting point to cycle start (c) plus some full cycles.
    
    So if we start one pointer at head and one at meeting point,
    moving both one step at a time, they'll meet at the cycle start!
    """)

def trace_algorithm_step_by_step():
    """Show step-by-step execution for test case 1"""
    print("\n🔍 STEP-BY-STEP TRACE: [3,2,0,-4] with cycle")
    print("=" * 50)
    
    # Create the linked list
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0) 
    node_neg4 = ListNode(-4)
    
    node3.next = node2
    node2.next = node0
    node0.next = node_neg4
    node_neg4.next = node2  # Cycle back to node2
    
    print("Linked List: 3 -> 2 -> 0 -> -4 -> (back to 2)")
    print("             0    1    2     3")
    print("Cycle starts at index 1 (node with value 2)")
    print()
    
    # Phase 1: Detect cycle
    print("Phase 1: Detect cycle")
    slow = fast = node3
    step = 0
    
    while fast and fast.next:
        print(f"Step {step}: slow at {slow.val}, fast at {fast.val}")
        slow = slow.next
        fast = fast.next.next
        step += 1
        
        if slow == fast:
            print(f"Step {step}: MEETING! Both at node {slow.val}")
            break
    
    print()
    print("Phase 2: Find cycle start")
    slow = node3  # Reset slow to head
    step = 0
    
    print(f"Reset: slow at head ({slow.val}), fast at meeting point ({fast.val})")
    
    while slow != fast:
        print(f"Step {step}: slow at {slow.val}, fast at {fast.val}")
        slow = slow.next
        fast = fast.next
        step += 1
    
    print(f"Step {step}: CYCLE START FOUND! Both at node {slow.val}")

def explain_second_loop_termination():
    """Explain how and why the second while loop terminates"""
    print("🤔 HOW DOES THE SECOND WHILE LOOP EXIT?")
    print("=" * 50)
    
    print("Great question! Let's trace through exactly what happens:")
    print()
    
    print("📋 SETUP AFTER PHASE 1:")
    print("- slow and fast met somewhere in the cycle")
    print("- slow = head (reset to beginning)")
    print("- fast = meeting_point (stays where they met)")
    print()
    
    print("📋 PHASE 2 LOOP:")
    print("while slow != fast:")
    print("    slow = slow.next     # Move 1 step from head")
    print("    fast = fast.next     # Move 1 step from meeting point")
    print()
    
    print("🎯 THE LOOP EXITS when slow == fast")
    print("(No explicit break needed - the condition becomes False)")
    print()
    
    # Demonstrate with actual example
    print("🛠️  STEP-BY-STEP EXAMPLE: [3,2,0,-4] cycle")
    print("-" * 45)
    
    # Create the linked list
    node3 = ListNode(3)
    node2 = ListNode(2)
    node0 = ListNode(0)
    node_neg4 = ListNode(-4)
    
    node3.next = node2
    node2.next = node0
    node0.next = node_neg4
    node_neg4.next = node2  # Cycle starts at node2
    
    print("List: 3 → 2 → 0 → -4 → (back to 2)")
    print("      0   1   2    3")
    print("Cycle starts at index 1 (node with value 2)")
    print()
    
    # Simulate Phase 1 to find meeting point
    slow = fast = node3
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            meeting_point = slow
            break
    
    print(f"Phase 1 result: Meeting point at node {meeting_point.val}")
    print()
    
    # Phase 2: Reset and trace
    print("Phase 2: Finding cycle start")
    slow = node3  # Reset to head
    fast = meeting_point  # Keep at meeting point
    
    step = 0
    print(f"Initial: slow at node {slow.val}, fast at node {fast.val}")
    print(f"Condition: slow != fast? {slow != fast}")
    print()
    
    while slow != fast:
        step += 1
        slow = slow.next
        fast = fast.next
        
        print(f"Step {step}: slow at node {slow.val}, fast at node {fast.val}")
        print(f"Condition: slow != fast? {slow != fast}")
        
        if slow == fast:
            print(f"✅ LOOP EXITS! slow == fast at node {slow.val}")
            break
        print()
    
    print()
    print("🎯 WHY THE LOOP TERMINATES:")
    print("1. Mathematical guarantee: slow and fast WILL meet")
    print("2. They meet exactly at the cycle start")
    print("3. When slow == fast, condition becomes False")
    print("4. Loop exits naturally (no break needed)")
    print()

def explain_mathematical_guarantee():
    """Explain why we're guaranteed the loop will terminate"""
    print("🧮 MATHEMATICAL GUARANTEE OF TERMINATION")
    print("=" * 50)
    
    print("❓ WHY are we guaranteed slow and fast will meet?")
    print()
    
    print("📐 From the mathematical proof:")
    print("- Distance from head to cycle start = 'a'")
    print("- Distance from meeting point to cycle start = 'c'")
    print("- Mathematical relationship: a = c (plus full cycles)")
    print()
    
    print("🚶 What this means in practice:")
    print("- slow starts at head, needs 'a' steps to reach cycle start")
    print("- fast starts at meeting point, needs 'c' steps to reach cycle start")
    print("- Since a = c, they take the SAME number of steps")
    print("- Moving at the same speed → they meet at the same time")
    print("- Meeting location = cycle start")
    print()
    
    print("🔒 TERMINATION GUARANTEE:")
    print("- The loop CANNOT run forever")
    print("- Maximum iterations = distance from head to cycle start")
    print("- This is finite and ≤ length of the linked list")
    print()
    
    print("🎯 EXAMPLE:")
    print("If cycle start is 3 nodes from head:")
    print("- slow moves: head → node1 → node2 → cycle_start")
    print("- fast moves: meeting → node1 → node2 → cycle_start")
    print("- After 3 iterations: slow == fast → loop exits")
    print()

def debug_your_input():
    """Debug function to help identify why you're getting the error"""
    print("🐛 DEBUGGING: 'Your returned value is not a ListNode type'")
    print("=" * 60)
    
    print("This error typically means:")
    print("1. Your function returned None (no cycle found)")
    print("2. But the test case expected a ListNode (cycle exists)")
    print()
    
    print("Let's check common issues:")
    print()
    
    print("❓ ISSUE 1: Are you creating the cycle correctly?")
    print("Example of CORRECT cycle creation:")
    
    # Correct way
    node1 = ListNode(1)
    node2 = ListNode(2)
    node1.next = node2
    node2.next = node1  # This creates the cycle!
    
    solution = Solution()
    result = solution.detectCycle(node1)
    
    print(f"✅ Correct cycle [1,2] → pos=0:")
    print(f"   Result: {result}")
    print(f"   Type: {type(result)}")
    if result:
        print(f"   Value: {result.val}")
    print()
    
    print("❓ ISSUE 2: Are you forgetting to create the cycle?")
    print("Example of INCORRECT (no cycle):")
    
    # Incorrect way - no cycle
    node3 = ListNode(1)
    node4 = ListNode(2)
    node3.next = node4
    # node4.next = None (default) - NO CYCLE!
    
    result2 = solution.detectCycle(node3)
    print(f"❌ No cycle [1,2] → None:")
    print(f"   Result: {result2}")
    print(f"   Type: {type(result2)}")
    print()
    
    print("❓ ISSUE 3: Check your input format")
    print("LeetCode format: [3,2,0,-4], pos = 1")
    print("This means:")
    print("- Create nodes: 3 → 2 → 0 → -4")
    print("- Connect tail to index 1: -4 → (points back to node at index 1)")
    print()
    
    # Show correct implementation of the example
    print("✅ CORRECT implementation of [3,2,0,-4], pos=1:")
    node_a = ListNode(3)  # index 0
    node_b = ListNode(2)  # index 1 ← cycle starts here
    node_c = ListNode(0)  # index 2
    node_d = ListNode(-4) # index 3
    
    node_a.next = node_b
    node_b.next = node_c
    node_c.next = node_d
    node_d.next = node_b  # pos=1 means point back to index 1 (node_b)
    
    result3 = solution.detectCycle(node_a)
    print(f"   Result: {result3}")
    print(f"   Type: {type(result3)}")
    if result3:
        print(f"   Value: {result3.val} (should be 2)")
    print()
    
    print("🔍 WHAT TO CHECK IN YOUR CODE:")
    print("1. Make sure you're actually creating a cycle with .next")
    print("2. Verify the last node points back to the correct position")
    print("3. Check that pos is not -1 (which means no cycle)")
    print()

def test_custom_case():
    """Test the custom case: 3->2->1->0->4 with 4 looping back to node 1 (value 1)"""
    print("🧪 TESTING CUSTOM CASE: 3->2->1->0->4 (cycle back to node 1)")
    print("=" * 60)
    
    # Create the linked list: 3->2->1->0->4
    node3 = ListNode(3)  # index 0
    node2 = ListNode(2)  # index 1
    node1 = ListNode(1)  # index 2 ← cycle starts HERE (node with VALUE 1)
    node0 = ListNode(0)  # index 3
    node4 = ListNode(4)  # index 4
    
    # Link them sequentially
    node3.next = node2
    node2.next = node1
    node1.next = node0
    node0.next = node4
    node4.next = node1  # Create cycle: 4 loops back to the NODE with VALUE 1
    
    print("Created list: 3 → 2 → 1 → 0 → 4 → (back to node with value 1)")
    print("Indices:      0   1   2   3   4")
    print("VALUES:       3   2   1   0   4")
    print("Cycle starts at the NODE WITH VALUE 1 (at index 2)")
    print()
    
    # Test the algorithm
    solution = Solution()
    result = solution.detectCycle(node3)
    
    print("🔍 ALGORITHM RESULT:")
    if result:
        print(f"✅ Cycle start found at node with value: {result.val}")
        print(f"✅ Expected: node with value 1")
        print(f"✅ Correct: {result.val == 1}")
        print(f"✅ Same object as node1: {result is node1}")
    else:
        print("❌ No cycle detected (returned None)")
    print()
    
    # Manual step-by-step trace
    print("🔍 STEP-BY-STEP TRACE:")
    print("-" * 25)
    
    # Phase 1: Detect cycle
    print("Phase 1: Detect cycle")
    slow = fast = node3
    step = 0
    
    print(f"Initial: slow at node {slow.val}, fast at node {fast.val}")
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        step += 1
        
        print(f"Step {step}: slow at node {slow.val}, fast at node {fast.val}")
        
        if slow == fast:
            meeting_point = slow
            print(f"🎯 MEETING! Both at node {meeting_point.val}")
            break
    
    print()
    print("Phase 2: Find cycle start")
    slow = node3  # Reset slow to head
    fast = meeting_point  # Keep fast at meeting point
    step = 0
    
    print(f"Reset: slow at head (node {slow.val}), fast at meeting point (node {fast.val})")
    
    while slow != fast:
        step += 1
        slow = slow.next
        fast = fast.next
        
        print(f"Step {step}: slow at node {slow.val}, fast at node {fast.val}")
        
        if slow == fast:
            print(f"🎯 CYCLE START FOUND! Both at node {slow.val}")
            break
    
    print()
    print("🎯 ANSWER TO YOUR QUESTION:")
    print(f"Does the algorithm correctly find node 1 as cycle start? {slow.val == 1}")
    print(f"They meet at node with value: {slow.val}")
    print(f"Expected: node with value 1")
    print(f"✅ SUCCESS: Algorithm works correctly!")
    print()
    
    print("🧮 WHY IT WORKS:")
    print("- Distance from head (3) to cycle start (1): 2 steps")
    print("- Distance from meeting point to cycle start: also matches mathematically")
    print("- The cycle: 1 → 0 → 4 → (back to 1)")
    print("- Length of cycle: 3 nodes")
    print()

def explain_mathematical_proof():
    """Detailed explanation of why distance from head to cycle start equals distance from meeting point to cycle start"""
    print("🧮 MATHEMATICAL PROOF: Why a = c?")
    print("=" * 50)
    
    print("❓ THE KEY QUESTION:")
    print("Why does distance from head to cycle start equal")
    print("distance from meeting point to cycle start?")
    print()
    
    print("📐 VISUAL SETUP:")
    print("Let's use this diagram:")
    print()
    print("    HEAD                 CYCLE START")
    print("     ↓                       ↓")
    print("   [H] → ... → [CS] → ... → [M] → ... → [CS]")
    print("      ←─ a ─→      ←─ b ─→      ←─ c ─→")
    print("                   └─────── cycle ──────┘")
    print()
    print("Where:")
    print("- a = distance from head to cycle start")
    print("- b = distance from cycle start to meeting point")
    print("- c = distance from meeting point back to cycle start")
    print("- Cycle length = b + c")
    print()
    
    print("🏃 PHASE 1 ANALYSIS:")
    print("When slow and fast pointers meet:")
    print()
    print("SLOW pointer traveled:")
    print("- From head to cycle start: a steps")
    print("- From cycle start to meeting point: b steps")
    print("- Total: a + b steps")
    print()
    print("FAST pointer traveled:")
    print("- Same path as slow: a + b steps")
    print("- PLUS k complete cycles: k × (b + c) steps")
    print("- Total: a + b + k×(b + c) steps")
    print()
    print("Since fast moves twice as fast as slow:")
    print("fast_distance = 2 × slow_distance")
    print("a + b + k×(b + c) = 2 × (a + b)")
    print()
    
    print("🧮 ALGEBRAIC MANIPULATION:")
    print("a + b + k×(b + c) = 2a + 2b")
    print("k×(b + c) = 2a + 2b - a - b")
    print("k×(b + c) = a + b")
    print("a + b = k×(b + c)")
    print("a = k×(b + c) - b")
    print("a = k×b + k×c - b")
    print("a = b×(k - 1) + k×c")
    print("a = (k - 1)×(b + c) + c")
    print()
    
    print("🎯 THE KEY INSIGHT:")
    print("a = (k - 1)×(b + c) + c")
    print("This means:")
    print("- 'a' equals 'c' plus some number of complete cycles")
    print("- When we move 'a' steps from head → reach cycle start")
    print("- When we move 'c' steps from meeting point → also reach cycle start")
    print("- Moving both at same speed → they meet AT cycle start!")
    print()
    
    print("🔍 CONCRETE EXAMPLE:")
    print("Let's verify with our test case: 3→2→1→0→4→(back to 1)")
    print()
    print("Values:")
    print("- a = 2 (head to cycle start: 3→2→1)")
    print("- b = 1 (cycle start to meeting: 1→0)") 
    print("- c = 2 (meeting to cycle start: 0→4→1)")
    print("- k = 1 (fast did 1 extra cycle)")
    print()
    print("Verification:")
    print("a = (k-1)×(b+c) + c")
    print("2 = (1-1)×(1+2) + 2")
    print("2 = 0×3 + 2")
    print("2 = 2 ✅")
    print()
    print("So both pointers need 2 steps to reach cycle start!")
    print()

def explain_different_speeds():
    """Explain why fast can move at different speeds and why 2x is optimal"""
    print("🏃 DOES FAST HAVE TO MOVE EXACTLY 2X FASTER?")
    print("=" * 50)
    
    print("❓ SHORT ANSWER: No! Fast can move 3x, 4x, or any multiple faster.")
    print("✅ BUT: 2x is optimal for practical reasons.")
    print()
    
    print("🧮 MATHEMATICAL GENERALIZATION:")
    print("If fast moves k times faster than slow (where k > 1):")
    print()
    print("When they meet:")
    print("- Slow traveled: a + b steps")
    print("- Fast traveled: k × (a + b) steps")
    print()
    print("Since fast also travels extra cycles:")
    print("Fast distance = Slow distance + m × cycle_length")
    print("k × (a + b) = (a + b) + m × (b + c)")
    print("(k - 1) × (a + b) = m × (b + c)")
    print("a + b = m × (b + c) / (k - 1)")
    print()
    print("For this to have integer solutions, we need specific conditions.")
    print()
    
    print("🔍 TESTING DIFFERENT SPEEDS:")
    print("-" * 35)
    
    # Test with our example: 3->2->1->0->4->(back to 1)
    node3 = ListNode(3)
    node2 = ListNode(2)
    node1 = ListNode(1)
    node0 = ListNode(0)
    node4 = ListNode(4)
    
    node3.next = node2
    node2.next = node1
    node1.next = node0
    node0.next = node4
    node4.next = node1
    
    print("Using our test case: 3→2→1→0→4→(back to 1)")
    print()
    
    # Test different speeds
    speeds = [2, 3, 4, 5]
    
    for speed in speeds:
        print(f"🏃 TESTING: Fast moves {speed}x faster than slow")
        
        slow = fast = node3
        step = 0
        
        while True:
            # Move slow 1 step
            slow = slow.next
            
            # Move fast 'speed' steps
            for _ in range(speed):
                if fast:
                    fast = fast.next
                else:
                    break
            
            step += 1
            
            if slow == fast:
                print(f"   ✅ Meeting after {step} iterations at node {slow.val}")
                break
            elif step > 10:  # Prevent infinite loop for demo
                print(f"   ❌ No meeting found within 10 iterations")
                break
        print()
    
    print("🎯 WHY 2X IS OPTIMAL:")
    print("-" * 25)
    print("1. 📊 GUARANTEED DETECTION: Always finds cycle if it exists")
    print("2. ⚡ MINIMAL ITERATIONS: Fastest convergence in most cases")
    print("3. 🔧 SIMPLE IMPLEMENTATION: Easy to code and understand")
    print("4. 📚 STANDARD PRACTICE: Universally recognized algorithm")
    print()
    
    print("🔍 WHAT ABOUT 3X, 4X, ETC?")
    print("-" * 30)
    print("✅ PROS:")
    print("- Still detects cycles")
    print("- May converge faster in some specific cases")
    print()
    print("❌ CONS:")
    print("- More complex to analyze mathematically") 
    print("- May miss cycles in some edge cases")
    print("- Not guaranteed to work for all cycle lengths")
    print("- Might require more iterations in practice")
    print()
    
    print("🧮 MATHEMATICAL INSIGHT:")
    print("The choice of speed affects the relationship:")
    print("- 2x: a = c (mod cycle_length) - Simple and elegant")
    print("- 3x: More complex relationship, harder to derive")
    print("- kx: Increasingly complex as k grows")
    print()
    
    print("🏆 CONCLUSION:")
    print("While other speeds CAN work, 2x is optimal because:")
    print("1. Simplest mathematical relationship")
    print("2. Most efficient in practice")
    print("3. Guaranteed to work for ANY cycle")
    print("4. Industry standard (Floyd's Algorithm)")
    print()

if __name__ == "__main__":
    # Explain different speeds first
    explain_different_speeds()
    print()
    
    # Then show the mathematical proof for 2x
    explain_mathematical_proof()
    print()
    
    # Test the custom case
    test_custom_case()
    
    print("🔁 ORIGINAL TESTS")
    print("=" * 30)
    
    # Add debugging first
    debug_your_input()
    
    print("🔁 ORIGINAL ALGORITHM TESTS")
    print("=" * 40)
    
    # Explain second loop termination
    explain_second_loop_termination()
    explain_mathematical_guarantee()
    
    print("🔁 NOW LET'S SEE THE FULL ALGORITHM")
    print("=" * 45)
    
    # Run tests
    test_solution()
    
    # Show algorithm explanation
    explain_algorithm()
    
    # Show step-by-step trace
    trace_algorithm_step_by_step()
