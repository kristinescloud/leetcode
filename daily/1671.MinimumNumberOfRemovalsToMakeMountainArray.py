"""
Title: 1671. Minimum Number of Removals to Make Mountain Array

Difficulty: Hard

Topics: Array, Binary Search, Dynamic Programming, Greedy

Description: https://leetcode.com/problems/minimum-number-of-removals-to-make-mountain-array/description/?envType=daily-question&envId=2024-10-30

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
DISCUSSION:

This is the kind of problem that you really need to break down into components before the way forward becomes clear. For this problem the break down
requires a bit of math and some reframing:

In order to find the minimum number of removals needed to make the given array, nums, into a mountain array the most obvious approach would be to find
the number of removals needed for every possible mountain peak, and then choose the smallest one. The question then becomes how do we efficiently find
the number of removals needed for a single mountain peak. Recall that the peak of a mountain array (called mountain), is an element of mountain such that:
    - mountain[peak_index] > mountain[peak_index + 1] > ... > mountain[len(mountain) - 1] > mountain[len(mountain)] (strictly decreasing sequence ending at peak_index)
    - mountain[0] < mountain[1] < ... < mountain[peak_index - 1] < mountain[peak_index] (strictly increasing sequence ending at peak_index)

Let i be the index of a possible peak of nums

Let lenLIS be length of longest strictly increasing subsequence (LIS) ending at i (including i)
Let lenLDS be length of longest strictly decreasing subsequence (LDS) starting at i
Let left be the left portion nums ending with the element at i
Let right be the right portion nums starting with the element at i
Let removals_left be the number of element removals needed in left to make it a valid left portion of a mountain array
Let removals_right be the number of element removals needed in right to make it a valid right portion of a mountain array
Let removals be the total number of elements removals needed to make nums a mountain array with peak nums[i]

left = nums[:i + 1] and therefore contains i + 1 elements
right = nums[i:] and therefore contains N - i elements

removals_left = # of elements in left - # elements in the LIS ending at i
              = len(left) - lenLIS
              = i + 1 - lenLIS

removals_right = # of elements in right - # elements in the LDS starting at i
               = len(right) - lenLDS
               = N - i - lenLDS 

removals = removals_left + removals_right
         = (i + 1 - lenLIS) + (N - i - lenLDS)
         = N + 1 - lenLIS - lenLDS

This illustrates that the number of removals needed to make nums a moutain array with peak nums[i], can be easily calculated if we have lenLIS and 
lenLDS for index i. Furthermore, to find the solution of this problem we evaluate all indexes as a potential peak and calculate the needed removals 
using the values of lenLIS and lenLDS at each index.

In breaking this problem down, we can appreciate that the problem is now to find the lenLIS and lenLDS for each index which is just the Longest Increasing 
Subsequence problem (LC (300.)). Perfect example of a problem that is almost indentical to another problem just with some extra steps.
"""

"""
APPROACH: Dynamic Programming to Find Longest Increasing Subsequence

INTUITION: See LC (300.)

    ALGORITHM:
        - Define a function length_of_LIS(nums, increasing=True):
            - If the increasing boolean is True we want this function to return a list containing the lengths of the longest increasing subsequence 
            ENDING at each index
                -  To do this the outer loop index, i, ranges from 0 to n - 1 (n is the number of elements in the nums array) and the inner loop index, j,
                ranges from 0 to i - 1.
            - If the increasing boolean is False we want this function to return a list containing the lengths of the longest decreasing subsequence 
            STARTING at each index
                -  To do this the outer loop index, i, ranges from n - 1 to 0 (n is the number of elements in the nums array) and the inner loop index, j,
                ranges from i + 1 to n - 1.
            - Return the dp array once the nested loops complete
            - See LC (300.) for more details
        - For the main solution function minimumMountainRemovals(nums):
            - Set the integer that will hold the minimum removals (called min_removals) to 1001 (since nums has a max size of 1000)
            - Call length_of_LIS(nums, increasing=True) and store the resulting array as lenLIS
            - Call length_of_LIS(nums, increasing=False) and store the resulting array as lenLDS
            - Loop through all indices of nums:
                - Check that lenLDS[index] and lenLIS[index] are greater than 1 (the peak cannot be the first or last element of the resulting mountain array):
                    - If so, update min_removals with min(min_removals,  N + 1 - lenLIS[index] - lenLDS[index])
                        - This compares the current minimum number of removals with the number of removal needed to make the current index the peak index
            - Return min_removals

COMPLEXITY:
    TIME: O(n^2), where n is the number of elements in the nums array
        - The major contributors to the time complexity are the calls made to length_of_LIS() and the loop that updates the min_removals as we iterate 
        through nums
            - One call to length_of_LIS() takes O(n^2) time (for details see LC (300.))
            - There are n elements in nums so looping through it takes O(n) time
        - Therefore the overall time complexity is O(2*n^2 + n) which simplifies to O(n^2)
    SPACE: O(n), where n is the number of elements in the nums array
        - The major contributors to the space complexity are the lenLIS and lenLDS arrays, which each have n elements
        - This makes the overall space complexity O(2*n) which simplifies to O(n)
"""
class Solution1:
    def length_of_LIS(self, nums, increasing=True):
        N, max_length = len(nums), 1
        dp = [1] * N
        
        outer_range = (range(N) if increasing else range(N - 1, -1, -1))
        for i in outer_range:
            inner_range = (range(i) if increasing else range(i + 1, N))
            for j in inner_range:
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    if dp[j] == max_length: break
            max_length = max(max_length, dp[i])
        
        return dp

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        min_removals, N = 1001, len(nums)
        lenLIS = self.length_of_LIS(nums, increasing = True) # array of LIS for each index
        lenLDS = self.length_of_LIS(nums, increasing = False) # array of LDS for each index

        for i in range(N):
            if lenLIS[i] > 1 and lenLDS[i] > 1: # if i is a valid peak
                min_removals = min(min_removals, N + 1 - lenLIS[i] - lenLDS[i])

        return min_removals
    
"""
APPROACH: Binary Search to Find Longest Increasing Subsequence

INTUITION: See LC (300.)

    ALGORITHM:
        - Define a function length_of_LIS(nums, increasing=True):
            - Create an array of the same length as nums, called len_LIS, that will store the longest subsequence encountered after arriving at i
            - After processing the number at an index i, update len_LIS[i] with the current length of the subsequence.
            - After the loop, if the increasing boolean is True, then we return len_LIS, otherwise, we return len_LIS reversed
            - See LC (300.) for more details
        - For the main solution function minimumMountainRemovals(nums):
            - Set the integer that will hold the minimum removals (called min_removals) to 1001 (since nums has a max size of 1000)
            - Call length_of_LIS(nums, increasing=True) and store the resulting array as lenLIS
            - Call length_of_LIS(nums, increasing=False) and store the resulting array as lenLDS
            - Loop through all indices of nums:
                - Check that lenLDS[index] and lenLIS[index] are greater than 1 (the peak cannot be the first or last element of the resulting mountain array):
                    - If so, update min_removals with min(min_removals,  N + 1 - lenLIS[index] - lenLDS[index])
                        - This compares the current minimum number of removals with the number of removal needed to make the current index the peak index
            - Return min_removals

COMPLEXITY:
    TIME: O(n*log(n)), where n is the number of elements in the nums array
        - The major contributors to the time complexity are the calls made to length_of_LIS(), the reversal of nums, and the loop that updates the 
        min_removals as we iterate through nums
            - One call to length_of_LIS() takes O(n*log(n)) time (for details see LC (300.))
            - One reversal of nums or lenLDS takes O(n) time since both arrays have n elements
            - There are n elements in nums so looping through it takes O(n) time
        - Therefore the overall time complexity is O(2*n*log(n) + 3*n) which simplifies to O(n*log(n))
    SPACE: O(n), where n is the number of elements in the nums array
        - The major contributors to the space complexity are the lenLIS and lenLDS arrays, which each have n elements
        - This makes the overall space complexity O(2*n) which simplifies to O(n)
"""
    
class Solution2:
    def length_of_LS(self, nums, increasing=True):
        N = len(nums)
        lenLIS = [1] * N # list of longest subsequence encountered at i
        LIS = [nums[0]] # current longest subsequence
        
        for i in range(1, N):
            pos = bisect.bisect_left(LIS, nums[i])
            if pos == len(LIS):
                LIS.append(nums[i])
            else:
                LIS[pos] = nums[i]
            lenLIS[i] = len(LIS)

        return lenLIS if increasing else lenLIS[::-1]

    def minimumMountainRemovals(self, nums: List[int]) -> int:
        min_removals, N = 1001, len(nums)
        lenLIS = self.length_of_LS(nums, increasing = True) # array of LIS for each index
        lenLDS = self.length_of_LS(nums[::-1], increasing = False) # array of LDS for each index

        for i in range(N):
            if lenLIS[i] > 1 and lenLDS[i] > 1: # if i is a valid peak
                min_removals = min(min_removals, N + 1 - lenLIS[i] - lenLDS[i])

        return min_removals
    

if __name__=="__main__":
    print(Solution2())
