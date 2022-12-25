class Solution:
    def threeSumMulti(self, arr: list[int], target: int) -> int:
        arr.sort()
        counter = 0
        length = len(arr)
        for i in range(length-1,1,-1):
            j, k = 0, i - 1
            while j < k:
                if arr[j] + arr[k] + arr[i] > target:
                    k -= 1
                elif arr[j] + arr[k] + arr[i] < target:
                    j += 1
                else:
                    countJ, countK = 1,1
                    while (j + countJ) < k and arr[j+countJ] == arr[j]:
                        countJ += 1

                    while (k - countK) >= (j + countJ) and arr[k - countK] == arr[k]:
                        countK += 1
                        
                    if arr[j] == arr[k]:
                        counter += (((countJ + countK) * (countJ + countK - 1) ) // 2)
                    else:
                        counter += countJ*countK
                    j += countJ
                    k -= countK
                
        return int(counter%(10**9 + 7))


mySolution = Solution()
print(mySolution.threeSumMulti([1,1,2,2,2,2], 5))