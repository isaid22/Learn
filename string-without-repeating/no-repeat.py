
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index_map = {}
        left = 0
        max_length = 0

        for right in range(len(s)):
            if s[right] in char_index_map:
                left = max(left, char_index_map[s[right]] + 1)
            char_index_map[s[right]] = right
            max_length = max(max_length, right - left + 1)

        return max_length

if __name__ == "__main__":
    # Create solution instance
    solution = Solution()
    
    # Test cases
    test_cases = [
        "abcabcbb",
        "bbbbb", 
        "pwwkew",
        "",
        "dvdf"
    ]
    
    print("Testing Solution:")
    for test in test_cases:
        result = solution.lengthOfLongestSubstring(test)
        print(f"Input: '{test}' -> Output: {result}")