class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for n in nums:
            if n in dup:
                return True
            else:
                dup.add(n)
        return False