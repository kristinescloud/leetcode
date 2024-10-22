"""
Title: 2583. Kth Largest Sum in a Binary Tree

Difficulty: Medium

Topics: Tree, Breadth-First Search, Depth-First Search, Sorting, Binary Tree

Description: https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/?envType=daily-question&envId=2024-10-22

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
APPROACH: Depth-First Search

INTUITION: This smells like a DFS problem because we know we are going to have to visit every node in order to calculate the sums at each level, and 
we want to be able to easily keep track of what level of the tree we are currently on. The goal is to do a DFS traversal of the tree, keeping track of
the tree level we are currently on so that we can add the value of the current node to the sum at its corresponding tree level.

    ALGORITHM:
        - In the main solution function:
            - We need a data structure to store the level sums in a way that makes it easy to identify which sum belongs which level
                - A list, level_sums, will work perfectly for this because we can store the sum at level, i, at index i of the list.
                    - NOTE: Since we don't initially know how many levels there are, this list will start out empty and we will have to append 0 to the 
                    list everytime we encounter a new level (if it isn't already, this will become clear soon)
            - We will call a recursive function dfs() that will traverse the tree, while keeping track of the current level and updating the level_sums
            in level_sums
            - When the recursive function call returns, we check that there are at least k levels using the length of level_sums:
                - If there are not we return -1, and otherwise we continue
            - If we have at least k levels, we sort level_sums in descending order and return level_sums at index k - 1
        - In the dfs(currrent_level, current_node, level_sums) function:
            - The changing variables in this recursive problem are the current level, the current node, and the level_sums list so these are the parameters
            of the dfs function.
            - If the current node is None (the node that made the current recursive call had 1 or less children), we return
            - If the current length of level_sums is less than 1 + current_level, this means that there is no index in the level_sums list for the current
            level. 
                - In this case we append 0 to the level_sums list, creating a space to store the level sum at the current level
            - Now that we have a space to store the level sum at the current level, we can add the value of the current node to level_sums list at index
            current_level
            - To continue exploring the tree, we then recursively call the function on the left and right subtrees of the current node, passing 
            1 + current_level as the new current_level

COMPLEXITY:
    TIME: **O(n), where n is the number of nodes in the tree
        - DFS traversal means we are visiting every node to add their values to the appropriate level sum, and since there are n nodes this takes O(n) time
        - After running DFS, we have to sort the values in level_sums. In a well-balanced tree** the length of levels_sum should be around log(n), and we
        know Python's built in sort method runs in O(m*log(m)) time where m is the length of the list.
            - If the tree is well-balanced** then the length of the list is log(n) and this sort operation would take O(log(n)*log(log(n))) time
                - Overall O(n + log(n)*log(log(n))) simplifies to O(n)
            - NOTE: If the tree is not well balanced (an extreme example being a binary tree that is basically a linked-list), then in the worst case
            the length of the level_sums list would n which would make the sort operation O(n*log(n)).
                - Since O(n + n*log(n)) simplifies to O(n*log(n)), this means that the overall time complexity would become O(n*log(n)) if the tree were 
                as unbalanced as possible
    SPACE: **O(log(n)), where n is the number of nodes in the tree.
        - If the tree is well-balanced**, then the maximum number of recursive calls on the stack at any time is log(n)
        - We also need to store the sum at each level in an array, and in a well-balanced tree** there should be log(n) levels meaning the list also 
        takes O(log(n)) space.
        - NOTE: If the tree is not well-balanced then the worst-case space complexity is O(n) since there would be one node at each level

"""
class TreeNode: # Class definition for a binary tree node.
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution: # Beat 97.96% on Runtime
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = []
        self.dfs(0, root, level_sums)
        if len(level_sums) < k: return -1
        level_sums.sort(key=None, reverse=True)
        print(level_sums)
        return level_sums[k-1]
   
    def dfs(self, level_count: int, node: Optional[TreeNode], level_sums: List[int]) -> None:
        if not node:
            return 
        
        if len(level_sums) < level_count + 1: level_sums.append(0)
        
        level_sums[level_count] += node.val
        self.dfs(level_count + 1, node.left, level_sums)
        self.dfs(level_count + 1, node.right, level_sums)

    

if __name__=="__main__":
    def createTree(tree_list: List[int]) -> TreeNode:
        n = len(tree_list)
        temp = []
        for i in range(n):
            node = TreeNode(val=tree_list[i])
            temp.append(node)
        for i in range(n):
            node = temp[i]
            if 2 * i + 1 < n: node.left = temp[2 * i + 1]
            if 2 * i + 2 < n: node.right = temp[2 * i + 2]
        return temp[0]

    tree_list1 = [5,8,9,2,1,3,7,4,6]
    tree_list2 = [1,2,0,3]
    print(Solution().kthLargestLevelSum(root=createTree(tree_list1), k=2) == 13)
    print(Solution().kthLargestLevelSum(root=createTree(tree_list2), k=1) == 3)
