# Array-7

## Problem 1: Sum of the products of all possible Subsets

Given an array of n non-negative integers. The task is to find the sum of the product of elements of all the possible subsets. It may be assumed that the numbers in subsets are small and computing product doesn’t cause arithmetic overflow.

Example :

Input : arr[] = {1, 2, 3}

Output : 23

Possible Subset are: 1, 2, 3, {1, 2}, {1, 3},
                    {2, 3}, {1, 2, 3}

Products of elements in above subsets :
1, 2, 3, 2, 3, 6, 6

Sum of all products = 1 + 2 + 3 + 2 + 3 + 6 + 6
                   = 23

## Problem 2: Minimum word distance (https://leetcode.com/problems/shortest-word-distance/)

Provided a list of words and two words, return the shortest distance between these two words in the list.

Example:

Assume that words = ["practice", "makes", "perfect", "coding", "makes"].



Input: word1 = “coding”, word2 = “practice”

Output: 3

Input: word1 = "makes", word2 = "coding"

Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
