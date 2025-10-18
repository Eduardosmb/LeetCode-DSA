class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicS, dicT = {}, {}

        for c in s:
            if c not in dicS.keys():
                dicS[c] = 1
            else:
                dicS[c] += 1

        
        for c in t:
            if c not in dicT.keys():
                dicT[c] = 1
            else:
                dicT[c] += 1
                
        if dicS == dicT:
            return True
        return False