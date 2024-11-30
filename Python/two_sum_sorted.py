"""
Problem: Two Sum in Sorted Array

Given a sorted array of integers and a target sum, find two numbers in the array that add up to the target.
Return the indices of these two numbers (1-based indexing).
You may assume exactly one solution exists.

Example:
Input: numbers = [2, 7, 11, 15], target = 9
Output: [1, 2]
Explanation: numbers[0] + numbers[1] = 2 + 7 = 9, so we return [1, 2]

Time Complexity Goal: O(n)
Space Complexity Goal: O(1)

Hint: Since the array is sorted, try using two pointers (one from start, one from end)
"""

def find_two_sum(numbers, target):
    # TODO: Implement your solution here
    pass

# Test cases
def test_two_sum():
    # Test case 1: Basic case
    assert find_two_sum([2, 7, 11, 15], 9) == [1, 2], "Test case 1 failed"
    
    # Test case 2: Numbers in middle of array
    assert find_two_sum([1, 4, 5, 7, 11, 13], 12) == [3, 4], "Test case 2 failed"
    
    # Test case 3: Numbers at extremes
    assert find_two_sum([1, 2, 3, 4], 5) == [1, 4], "Test case 3 failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_two_sum()
