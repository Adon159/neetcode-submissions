class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx in range(len(nums)):
            for idx1 in range(idx+1,len(nums)):
                if nums[idx] + nums[idx1] == target:
                    return [idx,idx1]