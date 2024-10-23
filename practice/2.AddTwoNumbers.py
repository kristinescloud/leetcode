"""
Title: 2. Add Two Numbers

Difficulty: Medium

Topics: Linked List, Math, Recursion

Description: https://leetcode.com/problems/add-two-numbers/description/

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

INTUITION: Since we are performing an addition and the numbers as linked lists are stored in reverse, we want to start adding digits at the beginning
of the linked lists so that we can account for the appropriate carryover that will be used in the addition at the next digit position. This makes
an iterative approach attractive because it makes it easy to move through each digit position and add like we would normally.

    ALGORITHM:
        - Initialize pointers for the first nodes, in l1 and l2, and initialize an integer to store the carryover
            - The pointers are how we will traverse l1 and l2
        - Initialize an empty ListNode, called node_sum
            - The name of this ListNode will be the pointer that points to head of the linked list that stores the sum of l1 and l2
        - Initialize another pointer that will also point to the empty ListNode
            - This pointer represents the node we are currently on, and will allow us to traverse the linked list that stores our sum.
        - Since we don't know how long l1 and l2 are we must iterate through them using a while loop:
            - The loop invariant is `node1 or node2 or carry` which just means that so long as one of these values is not null, the loop should continue.
                - We know it will terminate because eventually we will run out of digits (node1 and node2 are null) and there will be no remaining 
                carryover (carry == 0).
            - If there is a digit at l1 (node1 is not null), we add its value to the value of the current node and move the node1 pointer to the next node in l1
            - If there is a digit at l2 (node2 is not null), we add its value to the value of the current node and move the node2 pointer to the next node in l2
            - If there is carryover (carry != 0), we add its value to the value of the current node
            - We reassign the carryover value to be the integer quotient of the current node value divided by 10 (the tens digit of the sum of the digits and carryover at this position)
            - We reassign the current node value to be the current node value modulo 10 (the units digit of the sum of the digits and carryover at this position)
            - Now that node1, node2, and carry all hold the new values they would hold at the start of the next iteration, we check the loop invariant again:
                - If it holds we know that our sum linked list will have a value at the next digit position, and therefore the current node needs a new ListNode 
                to point to with its .next instance variable. Basically we are creating a new ListNode for current_node.next to point to!
            - Once the node that the current node points to has been defined, we can move the current_node pointer to current_node.next.

COMPLEXITY:
    TIME: O(max(l1.length, l2.length) + 1), where max(l1.length, l2.length) is the length of the longer number.
        - We iterate through each digit of l1 and l2 simultaneously which means we iterate max(l1.length, l2.length) times. 
        - At each digit we do a series of operations and checks each with O(1) time.
        - Therefore the overall time complexity is O(max(l1.length, l2.length) + 1) 
    SPACE: O(max(l1.length, l2.length) + 1), where max(l1.length, l2.length) is the length of the longer number.
        - The only signifincant data structure that can contribute to the storage complexity here is the linked list storing the result of the addition.
            - The result of the addition can have at most max(l1.length, l2.length) + 1 digits (1 digit more than the longer number), and since
            we have ListNode objects for each digit, the overall space complexity is O(max(l1.length, l2.length) + 1).
"""
class ListNode: # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        node1, node2, carry = l1, l2, 0
        node_sum = ListNode()
        curr_node = node_sum

        while node1 or node2 or carry:
            if node1: 
                curr_node.val += node1.val
                node1 = node1.next
            if node2: 
                curr_node.val += node2.val
                node2 = node2.next
            if carry: curr_node.val += carry
            carry = curr_node.val // 10
            curr_node.val = curr_node.val % 10
            if node1 or node2 or carry:
                next_node = ListNode()
                curr_node.next = next_node
            curr_node = curr_node.next
        
        return node_sum
    

if __name__=="__main__":
    print(Solution())
