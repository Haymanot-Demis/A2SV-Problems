class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = pref.copy()
        for i in range(1, len(pref)):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr