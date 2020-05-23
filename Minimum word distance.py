'''
Time Complexity: O(n)
Space Complexity: O(1)
Did this code successfully run on Leetcode : Yes
Explanation:
Create 2 indexes i1 and i2 and use these to track the indexes of the 2 words.
There are 2 cases:
1) If word1 = words[i]
make i1 = i
2) If word2 = words[i]
make i2 = i
'''


class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        # indexes to keep track of word 1 and word2
        i1 = -1
        i2 = -1
        minDistance = math.inf
        for i in range(len(words)):
            # Found word 1 update the index
            if words[i] == word1:
                i1 = i

            # Found word 2 update the index
            if words[i] == word2:
                i2 = i

            # if both words found then find minDistance
            if i1 != -1 and i2 != -1:
                minDistance = min(minDistance, abs(i1 - i2))

        return minDistance