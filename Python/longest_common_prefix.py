import argparse
import json
from typing import List

class Solution:
    def longest_common_prefix(self, strs: List[str]) -> str:
        if len(strs) < 2:
            return strs[0]
        
        max_prefix_index = -1
        strs = sorted(strs, key=len)

        for i, letter in enumerate(strs[0]):
            for other_word in strs[1:len(strs)]:
                if letter != other_word[i]:
                    break
            else:
                max_prefix_index = max_prefix_index+1
                continue
            break
        return strs[0][0:max_prefix_index+1]

def main():
    solution = Solution()

    # Test case 1: Basic case with common prefix
    assert solution.longest_common_prefix(["flower", "flow", "flight"]) == "fl", "Test case 1 failed"
    
    # Test case 2: No common prefix
    assert solution.longest_common_prefix(["dog", "racecar", "car"]) == "", "Test case 2 failed"
    
    # Test case 3: Single string
    assert solution.longest_common_prefix(["hello"]) == "hello", "Test case 3 failed"
    
    # Test case 4: Empty strings
    assert solution.longest_common_prefix(["", ""]) == "", "Test case 4 failed"
    
    # Test case 5: All same strings
    assert solution.longest_common_prefix(["test", "test", "test"]) == "test", "Test case 5 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    main()
