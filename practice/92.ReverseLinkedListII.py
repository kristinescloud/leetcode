"""
Title: 92. Reverse Linked List II

Difficulty: Medium

Topics: Linked List

Description: https://leetcode.com/problems/reverse-linked-list-ii/description/

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

from typing import Optional

"""
APPROACH: Iteration

INTUITION: We can take the exact same approach that is taken when reversing an entire linked list, the only difference now is that we need to maintain
a reference for the last node before the segment to be reversed begins. This reference will be used to connect the left unreversed segment (if it exists)
to the start of the reversed segment.

    ALGORITHM:
    - Initialize reference left_node pointing to the head, reference prev_node which is initially None, and an integer pos that will keep track of the
    node we're on
    - Use a while loop to traverse the linked list until pos equals left (loop guard here is pos < left):
        - Assign prev_node to left_node
        - Assign left_node to left_node.next
        - Increment pos
    - When the while loop terminates, create a reference prev_temp pointing to prev_node, and a reference curr_node pointing to left_node
    - Use another while loop to traverse and reverse the segment of the linked list to be reversed (loop guard here is pos <= right):
        - See 206.ReverseLinkedList.py
    - When the while loop terminates we first check if prev_temp exists:
        - If it does, this means there is an unreversed segment to the left of the reversed segment, and we need to connect the two.
            - We can do this by setting prev_temp.next to prev_node since the last object prev_node references is the [right]th node
    - We then need to connect the reversed segment to the unreversed segment on its right (if it exists)
        - We can do this by setting left_node.next to curr_node, since the last object curr_node references is the node (or None) that comes after the
        [right]th node
    If left == 1 (no unreversed segment to the left) the head ends up moving during the reversal process so we return prev_node instead, otherwise though
    the head would be returned

COMPLEXITY:
    TIME: O(right), where right is the position of the last node in the segment to be reversed
        - We iterate through all the nodes up until the node at the [right]th position and performed O(1) operations at each one
        - Therefore the overall time complexity would be O(right * 1) which is just O(right)
    SPACE: O(1)
        - The linked list is modified in place so there are no auxilliary sequence data structures and the solution is also iterative so there are no
        recursive calls taking up space on the call_stack

"""
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        left_node, prev_node = head, None
        pos = 1

        while pos < left:
            if pos != left and left_node:
                prev_node = left_node
                left_node = left_node.next
                pos += 1

        prev_temp = prev_node # prev_temp points to the last node before the segment to be reversed begins
        curr_node = left_node

        while pos <= right:
            temp = curr_node.next
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = temp
            pos += 1
        
        if prev_temp: prev_temp.next = prev_node # the final thing prev_node points to is the [right]th node
        left_node.next = curr_node # the final thing curr_node points to is what comes after the [right]th node (could be None or another node)

        return (prev_node if left == 1 else head) # if left == 1, the head ends up moving during the reversal process so we return prev_node instead

if __name__=="__main__":
    print(Solution())
