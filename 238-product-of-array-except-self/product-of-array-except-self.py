class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # res = []

        # for i in range(len(nums)):
        #     val = 1
        #     for k in range(len(nums)):
        #         if i != k:
        #             val *= nums[k]
        #     res.append(val)

        # return res

        res = [1 for _ in range(len(nums))]

        pre = 1
        for i in range(len(nums)):
            res[i] *= pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res


        