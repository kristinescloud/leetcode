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

from typing import Optional

"""
APPROACH: Iteration

INTUITION: We want to iterate through the linked list and reassign the .next pointers at each node to complete the reversal. The main thing we need to 
make sure we avoid when reassigning pointers is losing references to nodes that we will need later.

    ALGORITHM:
        - If the given linked list is empty then we should return an empty linked list
        - We know we will need at least one pointer to keep track of the current node we're on (we'll call that pointer curr_node). From the definiton
        of a ListNode, we also know that every node only points to the next node in the list, so, in order to reassign the .next pointer of the current
        node to the previous node (i.e. reversing the list) we must maintain a pointer for the node preceding the current node (we'll call this pointer 
        prev_node).
        - To iterate though the linked list we use a while loop with the loop invariant being that the current node must exist (i.e. curr_node != None):
            - Maintain a reference to the node after the current node with another pointer (e.g. temp = curr_node.next)
            - Reassign the current node's .next pointer to the previous node
            - Move the pointer for the previous node from the previous node to the current node
            - Move the pointer for the current node from the current node to the reference to the current node's former .next node (i.e. curr_node = temp)
        - The while loop terminates when the current node is None (or when the preceding node is the last element of the original linked list)
            - Therefore, we return the final value of prev_node as the new head of the reversed linked list


COMPLEXITY:
    TIME: O(n), where n is the length of the linked list or the number of elements in the linked list
        - There are n nodes, we visit each one once and reassign our pointers which takes O(1) time.
        - Therefore the overall time complexity is O(n * 1) which is just O(n)
    SPACE: O(1)
        - We reverse our linked list in place (i.e. without any auxillary sequence data structures), and the only other variables are references to 
        specific nodes

"""
class ListNode: # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
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

"""
APPROACH: Recursion

INTUITION: We want to use recursion to move through the linked list until we get to the last element. That last element will be the new head of the list,
and on the way back from the recursive calls we will reverse the direction the .next pointer at each node

    ALGORITHM:
        - For the solution function reverseList(head):
            - Initialize a single element list consisiting of the head pointer (we will use this to pass the head pointer into the recursive function by
            reference). We'll call this list head_ref.
            - Call the recursive function passing head_ref in for the head parameter and passing in head for the node parameter (since we want to start
            traversing the list from the head)
            - Return head_ref[0] which is the modified head pointer.

        - For the recursive function reverseListRec(head, node):
            - We have two function parameters: head, which will refer to the pointer pointing to the head of the linked list, and node, which will point
            to the current node we're on as we move through the linked list.
                - Thes are our function parameters becuase these are the variables subject to change in our recursive problem
            - If the current node does not exist, we terminate this recursive call with a return (base case)
            - If the current node exists, but the node after it does not, this means we have reached the last node of the linked list (base case):
                - In this case, we update our head pointer to point to the current node, since the last node of the original linked list becomes the
                head in the reversed linked list
                - Once the head has been updated, we terminate this recursive call with a return
            - If both the current node and the next node exist:
                - We first want to make a recursive call on the the next node (i.e. reverseListRec(head, node.next)) so that we can find the last element 
                and reassign it as the head before we start reversing all the .next pointers.
                - Once that recursive call completes, we know that we still need to make the .next pointer of the node ahead point to the current node.
                    - Since we haven't yet reversed the .next pointer of the current node, we know it still points to the value that was ahead of it in
                    the original linked list. 
                    - Therefore, to get the node ahead of the current node (i.e. node.next) to point to the current node we can make the node ahead's 
                    .next pointer point to the current node (i.e. node.next.next = node)
                - We reassign the .next pointer of the current node to None
                    - Generally does not matter too much since the earlier nodes will overwrite it, but will be very important for the first node in
                    the original linked list since it should now point to nothing

COMPLEXITY:
    TIME: O(n), where n is the length of the linked list or the number of elements in the linked list
        - We visit each node in the list once until we reach the base case (the last element), which takes O(n) time
        - We revisit the first n - 1 nodes to complete their recursive calls, which takes O(n - 1) time
        - Therefore the overall time complexity is O(n + n - 1) which is just O(n)
    SPACE: O(n), where n is the length of the linked list or the number of elements in the linked list
        - While we only use a single element list to maintain a reference to the head, using recursion means using space for every recursive call put on
        the call stack.
            - We make a recursive call for every element of the list but the last one. This means the maximum amount of recursive calls on the call stack
            is n - 1 which makes the overall space complexity O(n - 1 + 1) which is just O(n).
"""
class Solution2:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_ref = [head]
        self.reverseListRec(head_ref, head)
        return head_ref[0]
    
    def reverseListRec(self, head: Optional[ListNode], node: Optional[ListNode]) -> None:
        if not node: return
        elif not node.next: 
            head[0] = node
            return
        else: 
            self.reverseListRec(head, node.next)
            node.next.next = node
            node.next = None

if __name__=="__main__":
    print(Solution1())
    print(Solution2())
