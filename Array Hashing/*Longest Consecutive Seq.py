class Solution:
    def longestConsecutive(self, nums):
        seq = set(nums)
        longest = 0
        for n in nums:
            if n-1 not in seq:
                length = 0
                while n+length in seq:
                    length += 1
                longest = max(longest,length)
        return longest