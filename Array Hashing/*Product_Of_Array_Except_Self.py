class Solution:
    def productExceptSelf(self, nums):
        #You must write an algorithm that runs in O(n) time 
        #without using the division operation
        '''
        prefix = [1]*(len(nums)+2)
        postfix = [1]*(len(nums)+2)
        for i in range(1,len(nums)+1):
            prefix[i] = nums[i-1]*prefix[i-1]
        for j in range(len(nums),0, -1):
            postfix[j] = nums[j-1]*postfix[j+1]
        res = [1]*len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i]*postfix[i+2]
        return res
        '''     
        #better solution, according to the following-up
        res = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]
        return res 
        