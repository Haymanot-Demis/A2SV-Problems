import collections
class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maxSum = 0
        left = 0
        right = 0
        basket1 = []
        basket2 = []
        length = len(fruits)
        count = 0

        while right < length:
            if not basket1:
                print(fruits[right], "inserted to 1")
                count += 1
                basket1.append(fruits[right])
                right += 1
            elif fruits[right] in basket1:
                print(fruits[right], "inserted to 1")
                count += 1
                basket1.append(fruits[right])
                right += 1
            elif not basket2:
                print(fruits[right], "inserted to 2")
                count += 1
                basket2.append(fruits[right])
                right += 1
            elif fruits[right] in basket2:
                print(fruits[right], "inserted to 2")
                count += 1
                basket2.append(fruits[right])
                right += 1
            else:
                maxSum = max(maxSum, right - left)
                if fruits[left] in basket1:
                    print(fruits[left], "removed from 1")
                    basket1.remove(fruits[left])
                else:
                    print(fruits[left], "removed from 1")
                    basket2.remove(fruits[left])
                print(basket1, basket2)
                left += 1
                count -= 1
        maxSum = max(maxSum, right - left)
        return maxSum