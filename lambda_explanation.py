"""
Demonstration of how lambda parameter works in sorted() function
"""

def demonstrate_lambda_parameter():
    nums2 = [4, 2, 2, 5]
    
    print("nums2 =", nums2)
    print("Indices:", list(range(len(nums2))))
    print()
    
    # Method 1: Using lambda (what we use in the solution)
    print("Method 1: Using lambda")
    indices_by_value = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
    print("Result:", indices_by_value)
    print()
    
    # Method 2: Using a regular function (equivalent)
    print("Method 2: Using regular function (equivalent)")
    def get_nums2_value(index):
        print(f"  get_nums2_value({index}) = nums2[{index}] = {nums2[index]}")
        return nums2[index]
    
    indices_by_value_2 = sorted(range(len(nums2)), key=get_nums2_value, reverse=True)
    print("Result:", indices_by_value_2)
    print()
    
    # Method 3: Manual step-by-step to show what happens
    print("Method 3: Manual step-by-step breakdown")
    indices = list(range(len(nums2)))
    print("Starting indices:", indices)
    
    # Create pairs of (index, value) to show the sorting process
    index_value_pairs = []
    for i in indices:
        value = nums2[i]
        index_value_pairs.append((i, value))
        print(f"Index {i} → nums2[{i}] = {value}")
    
    print("\nPairs (index, value):", index_value_pairs)
    
    # Sort by value (second element of tuple) in descending order
    sorted_pairs = sorted(index_value_pairs, key=lambda pair: pair[1], reverse=True)
    print("Sorted pairs by value (desc):", sorted_pairs)
    
    # Extract just the indices
    final_indices = [pair[0] for pair in sorted_pairs]
    print("Final sorted indices:", final_indices)
    
    # Verify all methods give same result
    print(f"\nAll methods match: {indices_by_value == indices_by_value_2 == final_indices}")


def show_lambda_equivalents():
    """Show different ways to write the same lambda function"""
    nums2 = [4, 2, 2, 5]
    
    print("Different ways to write the same key function:")
    print()
    
    # Original lambda
    result1 = sorted(range(len(nums2)), key=lambda i: nums2[i], reverse=True)
    print("1. lambda i: nums2[i]")
    print("   Result:", result1)
    
    # Named function
    def key_func(i):
        return nums2[i]
    result2 = sorted(range(len(nums2)), key=key_func, reverse=True)
    print("2. def key_func(i): return nums2[i]")
    print("   Result:", result2)
    
    # Lambda with different parameter name (same behavior)
    result3 = sorted(range(len(nums2)), key=lambda index: nums2[index], reverse=True)
    print("3. lambda index: nums2[index]")
    print("   Result:", result3)
    
    # Lambda with different parameter name
    result4 = sorted(range(len(nums2)), key=lambda x: nums2[x], reverse=True)
    print("4. lambda x: nums2[x]")
    print("   Result:", result4)
    
    print(f"\nAll equivalent: {result1 == result2 == result3 == result4}")


if __name__ == "__main__":
    print("=" * 60)
    print("LAMBDA PARAMETER EXPLANATION")
    print("=" * 60)
    print()
    
    demonstrate_lambda_parameter()
    
    print("\n" + "=" * 60)
    print()
    
    show_lambda_equivalents()