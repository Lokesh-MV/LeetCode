class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        for i in nums:
            if i in res:
                res[i] += 1
            else:
                res[i] = 1
        return (list(res.keys())[list(res.values()).index(max(res.values()))])                 

        