class Solution:
    def topKFrequent(self, nums, k):
        '''
        count = {}
        res = set()
        for i in nums:
            count[i] = 1 + count.get(i,0) #O(n)
        data = list(count.values()) #O(n)
        heapq.heapify(data) #O(logn)
        lis = heapq.nlargest(k,data,key=None) #O(klogn)
        for i in lis: # O(n2)
            for j in count: 
                if count[j] == i:
                    res.add(j) 
        return list(res) #O(n).
        #Overall : O(n2) ?
        '''
        #Better solution O(klogn)
        # count = {}
        # res = []
        # bucket = [[] for i in range(len(nums)+1)]
        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        # for n,i in count.items():
        #     bucket[i].append(n)
        
        # for i in range(len(bucket)-1,0,-1):
        #     for n in bucket[i]:
        #         res.append(n)
        #         if len(res) == k:
        #             return res

        count = {}
        for n in nums:
            count[n] = count.get(n,0) + 1
        tier = list(count.keys())
        tier.sort(key=lambda x:count[x],reverse=True)
        return tier[:k]
        