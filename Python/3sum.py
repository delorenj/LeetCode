"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
 

Constraints:

3 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List, Tuple

def threesum(n: List[int]) -> List[Tuple[int, int, int]]:
    # sort the list
    # set 3 pointers i, j, k
    # find how many tuple the lowest digit can make
    # each time a tuple is found, add to result list
    
    if len(n) < 3:
        return []

    n.sort()

    _print = lambda i,j,k: print([i, j, k], n)

    res = []
    for i in range(len(n)-2):
        if i>0 and n[i] == n[i-1]: continue
        j = i+1
        k = len(n)-1
        while j<k:
            sum = n[i]+n[j]+n[k]
            if sum < 0:
                current = n[j]
                while j<k and n[j] == current: j+=1
            elif sum > 0:
                current = n[k]
                while k>j and n[k] == current: k-=1
            else:
                res.append((n[i], n[j], n[k]))
                current = n[j]
                while j<k and n[j] == current: j+=1
                current = n[k]
                while k>j and n[k] == current: k-=1

        current = n[i]
        while i<j and n[i] == current: i+=1

    return res
            
        
        
r = threesum([-1,0,1,2,-1,-4])
print(f'Result: {r}')
r = threesum([0,1,1])
print(f'Result: {r}')
r = threesum([0,0,0])
print(f'Result: {r}')
