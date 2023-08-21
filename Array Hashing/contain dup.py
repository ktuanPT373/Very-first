class Solution:
    def containsDuplicate(self, nums):
        visited = set()
        for i in range(len(nums)):
            if nums[i] in visited:
                return True
            visited.add(nums[i])
        return False
# Running time : O(n)
# Space complexity : O(n)