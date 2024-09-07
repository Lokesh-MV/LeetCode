class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        res = list(i for i in list1 if i in list2)
        nums = []
        for i in res:
            x = list1.index(i) + list2.index(i)
            nums.append(x)
        result = dict(zip(res, nums))
        lastList = []
        for i in result:
            if result[i] == min(result.values()):
                lastList.append(i)
        return lastList
        
                    
                    
        