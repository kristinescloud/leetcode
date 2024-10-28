"""
Title: 2641. Cousins in Binary Tree II

Difficulty: Medium

Topics: Hash Table, Tree, Depth-First Search (DFS), Breadth-First Search (BFS), Binary Tree

Description: https://leetcode.com/problems/cousins-in-binary-tree-ii/description/?envType=daily-question&envId=2024-10-26

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
APPROACH: Breadth First Search or Depth First Search

INTUITION: To find the sum of a nodes cousins we need to main pieces of information: 1. the total sum of the nodes at that level and 2. the sum of the 
current node and its sibling (if it has one). With these two pieces of information, the sum of a nodes cousins simply entails subtracting the sum of
the siblings from the sum of the nodes at that level. To find the sum of the nodes at each level of the tree we can use a breadth-first search (BFS) or
a depth-first search (DFS), and the same goes for the reassignment of original node values to the sum of a node's cousins. This two pass approach intuitive
because the sum of the nodes at a level and the sum of a sibling pair at that same level are coupled values (i.e. you cannot get the sum of the nodes a 
a level, without calculating the sum of a pair of siblings on that level) that are conceptually easier to calculate in two separate processes. 

    ALGORITHM:
        - Initialize an empty or 0-filled list to store level sum values
        - Use DFS or BFS to traverse the tree and calculate the sum of nodes at each level (see LC 2583.)
        - Use DFS or BFS to traverse the tree again, calculate and reaasign node values to the sum of their cousins (see. dfs_valupdate() and second BFS
        pass in replaceValueInTree())
        - Return the modified tree

COMPLEXITY:
    TIME: O(n), where n is the number of nodes in the tree
        - There are n nodes in the tree and we visit each one twice. Once for the first pass and once for the second pass.
        - This means that the overall time complexity is O(2*n), which simplifies to O(n) time
    SPACE: O(log(n))(!), where n is the number of nodes in the tree, and log(n) is the approximate number of levels in a well balanced tree
        - log(n) represents the approximate number of levels in a well balanced tree, which corresponds to the length of the auxilliary level_sums array
        as well as the maximum possible number of calls on the recursive call stack.
        - Therefore the space complexity is O(log(n))(!).
        - NOTE(!) The stated space complexity only holds if the binary tree is well balanced, if it is not, then in the worst case we would need O(n)
        auxilliary space to store the sum of nodes at each level, we could have up to n calls on the recursive call stack (takes O(n) space), and (in the case of BFS) the
        queue can grow to hold all nodes at once (takes O(n) space).
            - This would change the overall space complexity to O(3*n) which simplifies to O(n) space.

"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution: # Accepted – Beats 20.95% on Runtime
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        level_sums = []
        q = deque()
        q.append(root)

        while q: # first pass (BFS), calculate the level sums
            level_sums.append(0)
            n = len(q)
            for i in range(n):
                node = q.popleft()
                level_sums[-1] += node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)

        q.append([root])
        curr_level = 0

        while q: # second pass (BFS), reassign the node values to sum of thier cousins
            n = len(q)
            for i in range(n):
                sibling_nodes = q.popleft()
                sibling_sum = sum(node.val for node in sibling_nodes)
                for node in sibling_nodes:
                    next_siblings = [] 
                    if node.left: next_siblings += [node.left]
                    if node.right: next_siblings += [node.right]
                    if next_siblings: q.append(next_siblings)
                    node.val = level_sums[curr_level] - sibling_sum
            curr_level += 1
        
        return root
    
class Solution2: # Beats 18.93% on Runtime
    def dfs_levelsum(self, level: int, level_sums: List[int], node: Optional[TreeNode]) -> None:
        if not node: return

        level_sums[level] += node.val
        self.dfs_levelsum(level + 1, level_sums, node.left)
        self.dfs_levelsum(level + 1, level_sums, node.right)

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        # first pass (DFS), calculate the level sums
        level_sums = [0] * pow(10, 5)
        self.dfs_levelsum(0, level_sums, root)
        
        q = deque()
        q.append([root])
        curr_level = 0

        while q: # second pass (BFS), reassign the node values to sum of thier cousins
            n = len(q)
            for i in range(n):
                sibling_nodes = q.popleft()
                sibling_sum = sum(node.val for node in sibling_nodes)
                for node in sibling_nodes:
                    next_siblings = [] 
                    if node.left: next_siblings += [node.left]
                    if node.right: next_siblings += [node.right]
                    if next_siblings: q.append(next_siblings)
                    node.val = level_sums[curr_level] - sibling_sum
            curr_level += 1
        
        return root
    
class Solution3: # Beats 58.50% on Runtime
    def dfs_levelsum(self, level: int, level_sums: List[int], node: Optional[TreeNode]) -> None:
        if not node: return

        level_sums[level] += node.val
        self.dfs_levelsum(level + 1, level_sums, node.left)
        self.dfs_levelsum(level + 1, level_sums, node.right)

    def dfs_valupdate(self, level: int, level_sums: List[int], node: Optional[TreeNode]) -> None:
        sibling_sum = ((0 if not node.left else node.left.val) + (0 if not node.right else node.right.val))

        if node.left: 
            node.left.val = level_sums[level + 1] - sibling_sum
            self.dfs_valupdate(level + 1, level_sums, node.left)
        if node.right:
            node.right.val = level_sums[level + 1] - sibling_sum
            self.dfs_valupdate(level + 1, level_sums, node.right)

    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root
        
        # first pass (DFS), calculate the level sums
        level_sums = [0] * pow(10, 5)
        self.dfs_levelsum(0, level_sums, root)
        
        # second pass (DFS), reassign the node values to sum of thier cousins
        root.val = level_sums[0] - root.val
        self.dfs_valupdate(0, level_sums, root)

        return root


class Solution4: # Beats 97.68% on Runtime
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return root

        # single pass (BFS), calculate level sums and reassign values to sum of thier cousins simultaneosly
        curr_levelsum = root.val
        q = deque([root])

        while q:
            n = len(q)
            next_levelsum = 0
            for i in range(n):
                node = q.popleft() # when when deque a node, its value should already be the sum of itself and any siblings
                node.val = curr_levelsum - node.val
                children_sibling_sum = ((0 if not node.left else node.left.val) + (0 if not node.right else node.right.val))
                if node.left:
                    next_levelsum += node.left.val
                    node.left.val = children_sibling_sum
                    q.append(node.left)
                if node.right:
                    next_levelsum += node.right.val
                    node.right.val = children_sibling_sum
                    q.append(node.right)
            curr_levelsum = next_levelsum
        
        return root
    

if __name__=="__main__":
    print(Solution())
