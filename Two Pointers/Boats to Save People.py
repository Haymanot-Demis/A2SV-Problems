#time 37
class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        length = len(people)
        left = 0
        right = length - 1
        count = 0
        people.sort(reverse=True)
        # if length == 1:
        #     return 1
        while left <= right:
            if left == right:
                count +=1
                break
            if people[left] + people[right] <= limit:
                left += 1
                right -= 1
            else:
                left += 1
            count +=1
        return count