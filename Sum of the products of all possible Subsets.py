'''
Solution - 1 (subsetsMaths)
Time Complexity: O(n) -> no of elements in set
Space Complexity: O(1)
Did this code successfully run on Leetcode : Yes
Explanation:
The product of the sum of all subsets is equal to ((1+element1).. (1+elementn)) -1
Eg = 1,2,3
(1+1)(2+1)(3+1)-1 = 23
Proof: a b => a +b +ab => (1+a) + b(1+a) -1 => (1+a) (1+b) -1

Solution - 2 (subsetsBackTrack)
Time Complexity: O(2^n * n) -> n for computing the product for each set
Space Complexity: O(n)
Did this code successfully run on Leetcode : Yes
Explanation:
Use backtracking to create all subsets of a set and find product once its created and add it to a global sum.
'''

import copy
class Solution:
    #solution-1
    def subsetsMaths(self, nums: List[int]) -> int:
            product = 1
            for num in nums:
                product *= (1 + num)
            return product - 1

    #Solution - 2
    def __init__(self):
        self.sum = 0

    def backtrack(self, solution: List[int], nums: List[int], state: List[int], index: int):
        # we will never have repeated elements hence just add

        if len(state) > 0:
            product = 1
            for i in range(0, len(state)):
                product *= state[i]
            self.sum += product

        for i in range(index, len(nums)):
            # add candidate
            state.append(nums[i])
            # backtrack
            self.backtrack(solution, nums, state, i + 1)
            # pops elements and adds combination, last pop will be an empty array and start with a new subtree
            # pop
            state.pop()

    def subsetsBackTrack(self, nums: List[int]) -> int:
        if nums == None:
            return []

        solution = []
        self.backtrack(solution, nums, [], 0)

        return self.sum