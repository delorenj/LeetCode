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

"""


def find_two_sum(numbers, target):
    left = 0
    right = len(numbers) - 1

    while right > 0 and left < right:
        print(f"l: {left}, r: {right}, s: {numbers[left]+numbers[right]}")
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left + 1, right + 1]
        elif sum < target:
            left = left + 1
        else:
            right = right - 1
    raise "Bad Data: No sum found, and you promised it would be there =("


# Test cases
def test_two_sum():
    # Test case 1: Basic case
    assert find_two_sum([2, 7, 11, 15], 9) == [1, 2], "Test case 1 failed"

    # Test case 2: Numbers in middle of array
    assert find_two_sum([1, 4, 5, 7, 11, 13], 12) == [1, 5], "Test case 2 failed"

    # Test case 3: Numbers at extremes
    assert find_two_sum([1, 2, 3, 4], 5) == [1, 4], "Test case 3 failed"

    print("All test cases passed!")


if __name__ == "__main__":
    test_two_sum()
