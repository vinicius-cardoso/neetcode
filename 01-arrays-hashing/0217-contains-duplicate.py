"""
217. Contains Duplicate  (Easy)
https://leetcode.com/problems/contains-duplicate/

Problem: return True if any value in the array appears at least twice.

Approach: hash set.
    Sorting first would work and needs no extra memory, but it costs
    O(n log n). A set buys O(1) average membership checks, so a single
    pass is enough. Trade memory for time — the standard deal in this
    whole topic.

Time:  O(n)  — one pass, set add/lookup are O(1) average
Space: O(n)  — the set holds up to n values

Note to self: my first instinct was the nested loop comparing every
pair, which is O(n^2). The signal to reach for a set is the phrase
"have I seen this before?" — whenever the question is about
*membership* rather than order or position, a set is the answer.
"""


def contains_duplicate(nums: list[int]) -> bool:
    seen = set()

    for num in nums:
        if num in seen:  # membership check is the whole trick
            return True
        seen.add(num)

    return False


if __name__ == "__main__":
    assert contains_duplicate([1, 2, 3, 1]) is True
    assert contains_duplicate([1, 2, 3, 4]) is False
    assert contains_duplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) is True
    assert contains_duplicate([]) is False   # edge: empty
    assert contains_duplicate([1]) is False  # edge: single element
    print("passed")
