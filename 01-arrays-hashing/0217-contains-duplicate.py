"""
217. Contains Duplicate  (Easy)

https://neetcode.io/problems/duplicate-integer/question?list=neetcode150
https://leetcode.com/problems/contains-duplicate/description/

Problem: return True if any value in the array appears at least twice.

Approach: hash set.
    Sorting first would work and needs no extra memory, but it costs
    O(n log n). A set buys O(1) average membership checks, so a single
    pass is enough. Trade memory for time — the standard deal in this
    whole topic.

Time:  O(n)  — one pass, set add/lookup are O(1) average
Space: O(n)  — the set holds up to n values

Note to self: my first instinct was just convert nums list to a set and compare 
the size of the list and set, but it will cost more memory, given that this 
solution will copy all the list.
"""

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False

if __name__ == "__main__":
    s = Solution()

    assert s.hasDuplicate([1,2,3,]) is False
    assert s.hasDuplicate([1,2,3,1]) is True
    assert s.hasDuplicate([]) is False
    assert s.hasDuplicate([1]) is False

    print("passed")
