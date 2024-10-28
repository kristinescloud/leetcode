"""
Title: 951. Flip Equivalent Binary Trees

Difficulty: Medium

Topics: Tree, Depth-First Search (DFS), Binary Tree

Description: https://leetcode.com/problems/flip-equivalent-binary-trees/?envType=daily-question&envId=2024-10-24

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
APPROACH: Depth-First Search (DFS)

INTUITION: We want to do a depth first search where we traverse two trees simultaneously and assess whether or not they are flip equivalent.

    ALGORITHM:
        - For the recursive dfs(node1, node2):
            - node1 and node2 reference the subtrees of the first and second trees, respectively, that are being called on
            - If both node1 and node2 are None, we return True
            - If node1 or node2 is None, we return False
            - If both nodes exist, but have different values, we return False
            - TODO #6


COMPLEXITY:
    TIME: O(n), where n is the minimum between n1, the number of nodes in the first tree, and n2 is the number of nodes in the second tree.
        - Since we have two trees that aren't necessarily the same size, the maximum amount nodes that we will have to visit will be the minimum between
        n1 and n2, because after the minimum it will become apparent if the two trees are flip equivalent or not (i.e. one tree having more values and
        the other tree not having any more values)
            - The recursion stops at the leaf nodes or when a mismatch occurs. Therefore, in the worst case, every node in the smaller tree will be visited.
    SPACE: O(n), where n is the minimum between n1, the number of nodes in the first tree, and n2 is the number of nodes in the second tree.
        - Since the solution is recursive, we take up space on the recursive call stack
        - As decribed above, the maximum amount nodes that we will have to visit will be the minimum between n1 and n2, and that the maximum amount nodes 
        that we will have to visit is also the maximum amount of recursive calls that could be on the call stack (occurs when the tree is very poorly
        balanced).
        - NOTE! If the tree is well balanced, the space complexity would be more like O(log(n)) since the tree's height would be logarithmic relative to 
        the number of nodes.

"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.dfs(root1, root2)

    def dfs(self, node1: Optional[TreeNode], node2: Optional[TreeNode]) -> bool:
        if not node1:
            if not node2: return True
            return False
        elif not node2: return False # if we get here we know node1 exists, so if node2 does not exist we return False
        else:
            if node1.val != node2.val: return False
            if self.dfs(node1.left, node2.left):
                return self.dfs(node1.right, node2.right)
            elif self.dfs(node1.left, node2.right):
                return self.dfs(node1.right, node2.left)
            else: return False

    

if __name__=="__main__":
    print(Solution())
