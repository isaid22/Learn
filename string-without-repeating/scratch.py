my_str = "abc"

for idx, chr in enumerate(my_str):
    print(f"Index: {idx}, Character: {chr}\n") 

# Your implementation to check
def findStringLength(s: str) -> int:
    observed = {} # declare a dictionary hash map like this: alphabet: idx
    left_idx = 0
    right_idx = 0
    longest_length = 0
    for right_idx, alphabet in enumerate(s):  
        if alphabet in observed and observed[alphabet] >= left_idx:  # Fixed: missing colon
            left_idx = observed[alphabet] + 1 # move left idx 
        
        observed[alphabet] = right_idx
        longest_length = max(longest_length, right_idx - left_idx + 1)  # Fixed: spacing
    return longest_length

# Test your implementation
def test_implementation():
    print("🧪 TESTING YOUR IMPLEMENTATION")
    print("=" * 50)
    
    test_cases = [
        ("abcabcbb", 3),    # Expected: 3 (abc)
        ("bbbbb", 1),       # Expected: 1 (b)
        ("pwwkew", 3),      # Expected: 3 (wke)
        ("", 0),            # Expected: 0 (empty)
        ("dvdf", 3),        # Expected: 3 (vdf)
        ("abc", 3),         # Expected: 3 (abc)
        ("a", 1),           # Expected: 1 (a)
    ]
    
    all_correct = True
    
    for test_str, expected in test_cases:
        result = findStringLength(test_str)
        correct = result == expected
        all_correct = all_correct and correct
        
        status = "✅" if correct else "❌"
        print(f"{status} Input: '{test_str}' -> Got: {result}, Expected: {expected}")
        
        if not correct:
            print(f"   ❌ FAILED: Expected {expected} but got {result}")
    
    print("\n" + "=" * 50)
    if all_correct:
        print("🎉 ALL TESTS PASSED! Your implementation is CORRECT!")
    else:
        print("❌ Some tests failed. Check the implementation.")
    
    return all_correct

# Step-by-step trace for debugging
def trace_algorithm(s: str):
    print(f"\n🔍 STEP-BY-STEP TRACE FOR: '{s}'")
    print("=" * 40)
    
    observed = {}
    left_idx = 0
    longest_length = 0
    
    print(f"Initial: observed={observed}, left_idx={left_idx}, longest_length={longest_length}")
    print()
    
    for right_idx, alphabet in enumerate(s):
        print(f"Step {right_idx + 1}: Processing '{alphabet}' at index {right_idx}")
        
        # Check if character was seen before
        if alphabet in observed and observed[alphabet] >= left_idx:
            old_left = left_idx
            left_idx = observed[alphabet] + 1
            print(f"  '{alphabet}' seen at index {observed[alphabet]} (>= {old_left})")
            print(f"  Move left_idx: {old_left} -> {left_idx}")
        else:
            if alphabet in observed:
                print(f"  '{alphabet}' seen at index {observed[alphabet]} (< {left_idx}) - ignore")
            else:
                print(f"  '{alphabet}' is new")
        
        # Update character position
        observed[alphabet] = right_idx
        
        # Calculate current window length
        current_length = right_idx - left_idx + 1
        old_longest = longest_length
        longest_length = max(longest_length, current_length)
        
        print(f"  observed: {observed}")
        print(f"  Current window: '{s[left_idx:right_idx+1]}' (length: {current_length})")
        print(f"  longest_length: max({old_longest}, {current_length}) = {longest_length}")
        print()
    
    print(f"🎯 Final result: {longest_length}")
    return longest_length

if __name__ == "__main__":
    # Test the implementation
    test_implementation()
    
    # Show detailed trace for one example
    trace_algorithm("abcabcbb") 