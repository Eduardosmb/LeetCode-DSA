class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        res = [0 for _ in range(len(temperatures))]
        stack = []

        for i, k in enumerate(temperatures):
            while stack and k > stack[-1][0]:
                stackT, stackI = stack.pop()
                res[stackI] = i - stackI

            stack.append([k, i])
        return res

        # res = []

        # for i in range(len(temperatures)):
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[i]  < temperatures[j]:
        #             res.append(j-i)
        #             break
        
        #     if len(res) == i:
        #         res.append(0)
        # return res