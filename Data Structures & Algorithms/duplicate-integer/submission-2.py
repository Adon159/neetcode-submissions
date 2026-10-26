class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        list1 = []

        for idx in range(len(nums)):
            if nums[idx] not in list1:
                list1.append(nums[idx])
            else:
                pass

        if len(list1) != len(nums):
            return True

        else:
            return False
        