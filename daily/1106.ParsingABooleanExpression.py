"""
Title: 1106. Parsing A Boolean Expression

Difficulty: Hard

Topics: String, Stack, Recursion

Description: https://leetcode.com/problems/parsing-a-boolean-expression/description/?envType=daily-question&envId=2024-10-20

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
Approach: Recursion

Intuition: It seems most feasible to evaluate the string character by character, while storing subexpressions in a list when we encounter an operator that 
can be applied on more than one value. To do this the current character can be defined at the start of the recursive call, using th expression and a 
reference to the index of the current character. Once the current character is defined we can keep the index value one step ahead of it 

For the recursion:
    - Base case: 
        - if the current character is 't': return True
        - if the current character is 'f': return False
    - Recursive steps:
        - if the current character is '!': 
            - we want to skip the '('
            - then we want to recursively call the function on the inner subexpression for ! (there will only be one), and then negate its result
            - we also want to skip the ')'
        - NOTE: if we get here we are dealing with an AND or OR operator as the current character and store all the recursively evaluated suexpressions
        in a list until we encounter the corresponding closing bracket.
        - if the current character is '&': if there exists only True values in the list return True otherwise return False
        - if the current character is '|': if theres exists a single True value in the ist return True otherwise return False
        - if the current character is not a valid character: return False (not possible due to constraints)

Complexity:
    - Time: O(n), where n is the length of the expression
        - Reasoning: Each character in the string is visited only once and at each character the operations done are O(1)
    - Space: O(n), where n is the length of the expression
        - Reasoning: If the expression is deeply nested, then the maximum number of recursive calls on the call stack is on the order of O(n).
        As well, storing the evaluate subexpressions in values also requires space that is bounded by O(n) (just means that no subexpression will exceed the length of th egreater expression)

"""

class Solution1:
    def parseBoolExpr(self, expression: str) -> bool:
        index = [0]
        return self.evaluate(expression, index)

    def evaluate(self, expr, index):
        curr_char = expr[index[0]]
        index[0] += 1 # index is one position ahead of curr_char

        if curr_char == 't': return True
        if curr_char == 'f': return False
        
        if curr_char == '!':
            index[0] += 1 # skips '('
            res = not self.evaluate(expr, index)
            index[0] += 1 # skips ')'
            return res
        
        # now we know we're dealing with AND '&(...)' and OR '|(...)'
        vals = []
        index[0] += 1 # skips '('
        while expr[index[0]] != ")":
            if expr[index[0]] != ",":
                vals.append(self.evaluate(expr, index))
            else:
                index[0] += 1 #skips commas
        index[0] += 1 # skips ')'

        if curr_char == '&':
            return all(vals)

        if curr_char == '|':
            return any(vals)

        return False

"""
Approach: Stack

Intuition: This approach uses a stack to model the nested structure of these expressions instead of recursion. What we can do is initialize an empty stack,
and then, going from left to right, push all operators, 't's, and 'f's onto the stack. When we encounter a closing parentheses, that means we have reached 
the end of a subexpression that we now need to evaluate so we pop all subexpressions on the stack until the corresponding operation character and then pop 
the operator to determine the operation performed on these newly popped stack elements. Push the result of the operation perfomed back onto the stack, and 
continue iteration through the expression accordingly.

Complexity:

"""


class Solution2:
    def somefunction() -> None:
        return None

if __name__=="__main__":
    print(Solution1())
