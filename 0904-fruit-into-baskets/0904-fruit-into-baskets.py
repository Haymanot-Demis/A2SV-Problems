import collections
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        maxSum = 0
        left = 0
        right = 0
        basket1 = {}
        basket2 = {}
        length = len(fruits)

        while right < length:
            if not basket1 or fruits[right] in basket1:
                basket1[fruits[right]] = basket1.get(fruits[right], 0) + 1
                right += 1
            elif not basket2 or fruits[right] in basket2:
                basket2[fruits[right]] = basket2.get(fruits[right], 0) + 1
                right += 1
            else:
                maxSum = max(maxSum, right - left)
                if fruits[left] in basket1:
                    while fruits[left] == fruits[left + 1]:
                        basket1[fruits[left]] -= 1
                        left += 1
                    basket1[fruits[left]] -= 1
                    if basket1[fruits[left]] == 0:
                        basket1.pop(fruits[left])
                    left += 1
                else:
                    while fruits[left] == fruits[left + 1]:
                        basket2[fruits[left]] -= 1 
                        left += 1
                    basket2[fruits[left]] -= 1
                    if  basket2[fruits[left]] == 0:
                        basket2.pop(fruits[left])
                    left += 1
        maxSum = max(maxSum, right - left)
        return maxSum