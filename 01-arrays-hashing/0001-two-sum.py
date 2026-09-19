"""
1. Two Sum  (Easy)

https://neetcode.io/problems/two-integer-sum/question?list=neetcode150
https://leetcode.com/problems/two-sum/

Problem: Given an array of integers nums and an integer target, return the 
indices i and j such that nums[i] + nums[j] == target and i != j.
You may assume that every input has exactly one pair of indices i and j that 
satisfy the condition.
Return the answer with the smaller index first.

Approach: One-pass hash map. The solution stores the complement itself 
(target - num) keyed by index, and checks whether the current number matches a 
complement seen earlier.

Time:  O(n)  — Single pass through 'nums' list.
Space: O(n)  — The hash map can hold up to n entries in the worst case.

Note to self: Another solution is use two pointers, but is not the optimal.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}

        for i, num in enumerate(nums):
            if num in hashmap:
                return [hashmap[num], i]
            hashmap[target-num] = i


if __name__ == "__main__":
    s = Solution()

    assert s.twoSum([3,4,5,6], 7) == [0,1]
    assert s.twoSum([4,5,6,10], 10) == [0,2]

    print("passed")
