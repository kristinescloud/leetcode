"""
Title: 206. Reverse Linked List

Difficulty: Easy

Topics: Linked List, Recursion

Description: https://leetcode.com/problems/reverse-linked-list/description/

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
APPROACH: 


INTUITION:

    ALGORITHM:


COMPLEXITY:
    TIME:
    SPACE:

"""
class ListNode: # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head
        prev_node = None
        curr_node = head

        while curr_node:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp

        return prev_node

if __name__=="__main__":
    print(Solution())
