class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dici = {}
        for i in range (len(nums)):
            diff = target - nums[i]
            if diff not in dici.keys():
                dici[nums[i]] = i
            else:
                return [dici[diff], i]
        return []