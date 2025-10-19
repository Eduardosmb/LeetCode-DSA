class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)


        longest = 0

        for n in numbers:
            if n-1 not in numbers:
                lenght = 1
                while n+lenght in numbers:
                    lenght+= 1
                longest = max(longest, lenght)

        return longest

