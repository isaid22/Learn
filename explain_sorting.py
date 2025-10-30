"""
Demonstration of sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
"""

def explain_index_sorting():
    nums2 = [4, 2, 2, 5]
    print("Original nums2:", nums2)
    print("Indices:       ", list(range(len(nums2))))
    print()
    
    # Step 1: Show what range(len(nums2)) gives us
    indices = list(range(len(nums2)))
    print("Step 1 - Create indices:")
    print(f"range(len(nums2)) = range({len(nums2)}) = {indices}")
    print()
    
    # Step 2: Show what each index maps to
    print("Step 2 - Show index → value mapping:")
    for i in indices:
        print(f"Index {i} → nums2[{i}] = {nums2[i]}")
    print()
    
    # Step 3: Show the sorting process
    print("Step 3 - Sort indices by their corresponding values (descending):")
    
    # Manual sorting to show the process
    index_value_pairs = [(i, nums2[i]) for i in indices]
    print("Index-value pairs:", index_value_pairs)
    
    # Sort by value (descending)
    sorted_pairs = sorted(index_value_pairs, key=lambda x: x[1], reverse=True)
    print("Sorted by value (desc):", sorted_pairs)
    
    # Extract just the indices
    result_indices = [pair[0] for pair in sorted_pairs]
    print("Final indices order:", result_indices)
    print()
    
    # Step 4: Verify with the actual function
    actual_result = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
    print("Using the actual function:")
    print(f"sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True) = {actual_result}")
    print()
    
    # Step 5: Show what this means
    print("What this result means:")
    print("We should process nums2 elements in this order to get largest values first:")
    for i, idx in enumerate(actual_result):
        print(f"Position {i}: Use index {idx}, which has value nums2[{idx}] = {nums2[idx]}")

def demonstrate_with_different_array():
    print("\n" + "="*60)
    print("Another example with different array:")
    
    nums2 = [1, 5, 3, 2, 4]
    print("nums2:", nums2)
    
    result = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
    print("Result:", result)
    
    print("\nThis means:")
    for i, idx in enumerate(result):
        print(f"{i+1}. Index {idx} has value {nums2[idx]}")

if __name__ == "__main__":
    explain_index_sorting()
    demonstrate_with_different_array()