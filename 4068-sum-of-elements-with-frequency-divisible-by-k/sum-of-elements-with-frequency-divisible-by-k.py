class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        dic = {}
        for n in nums:
            dic[n] = dic.get(n, 0) + 1

        res = 0
        for v, f in dic.items():
            if f%k == 0:
                res += v*f
        return res            