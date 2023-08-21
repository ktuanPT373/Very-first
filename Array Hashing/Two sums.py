class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i, n in enumerate(nums):
            dif = target - n
            if dif in hashmap:
                return [hashmap[dif],i]
            hashmap[n] = i
        return
        # O(n),O(n)

        # for i in range(len(nums)):
        #     dif = target - nums[i]
        #     for j in range(i+1,len(nums)):
        #         if nums[j] == dif:
        #             return [i,j]
        # return
        # O(n2), O(1)