class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count ={}
        for idx in nums:
            count.setdefault(idx,0)
            count[idx] = count.get(idx, 0) + 1


        sortedcount = sorted(count.keys(),key=lambda x:count[x], reverse =True)

        return sortedcount[:k]