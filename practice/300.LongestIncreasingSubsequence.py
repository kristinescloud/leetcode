"""
Title: 300. Longest Increasing Subsequence

Difficulty: Medium

Topics: Array, Binary Search, Dynamic Programming

Description: https://leetcode.com/problems/longest-increasing-subsequence/description/

"""
from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

"""
APPROACH: 1D Dynamic Programming

INTUITION: TODO #14

    ALGORITHM:

COMPLEXITY: TODO #15
    TIME: O(n^2), where n is the length of the given array nums
    SPACE: O(n), where n is the length of the given array nums

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        dp = [1] * N # a memory array where dp[i] the length of the longest increasing subsequence starting from index i
        len_longest = 1

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    if dp[j] == len_longest: break
            len_longest = max(len_longest, dp[i])

        return len_longest

"""
APPROACH: Binary Search

INTUITION: The strategy is to ensure that the length of this subsequence remains the same or increases with the addition of new elements. As we iterate 
through each element in the array nums, we can use binary search to find the index of the first element in our subsequence that is greater than or equal 
to the current element. If this index is equal to the size of the subsequence, it indicates that the current element is greater than the last element in 
the subsequence. Therefore, we add it to the subsequence, which increases its length. If the binary search yields an index within the existing subsequence, 
we replace the element at that index with the current element. This is done because the current element is either equal to or smaller than the existing 
element, and this allows for potentially more elements to be added to the subsequence in the future.

NOTE! If we wanted to return a valid longest increasing subsequence, this solution is not completely correct and this can be demostrated with inputs like
nums = [10,9,2,5,3,1] and nums = [10,9,2,5,3,1,7,101,18]. To ensure the return of a valid subsequence we can only allow the replacement of a substring
value to occur when the position returned from the binary search is the last index in the subsequence (pos == len(subseq) - 1).

    ALGORITHM: TODO #17

COMPLEXITY: TODO #16
    TIME: O(n*log(n)), where n is the length of the given array nums
    SPACE: O(n), where n is the length of the given array nums

"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        subseq = [] # subseq is initially in sorted order so we can use binary search on it
        for num in nums:
            pos = bisect.bisect_left(subseq, num)
            if pos == len(subseq): # num is greater than greatest element in subseq
                subseq.append(num)
            else: # num is less than the current value at subseq[pos]
                subseq[pos] = num # therefore we reassign subseq[pos] to num since any number that was greater than the previous value of subseq[pos] will also be greater than num and subseq[pos] being smaller may allow us to add more numbers into the subsequence later  
        return len(subseq)

if __name__=="__main__":
    print(Solution())
