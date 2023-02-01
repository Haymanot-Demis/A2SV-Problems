class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        """
        the idea is to make the value uniwue by incrementing it until its is no longer exists in the list twice to do that take the duplicated number, then it can't be less than the prevously incremented number so take that number count the number of moves needed toe make it there and then increment again until it is unique in the list 
        """
        moves = 0
        length = len(nums)
        nums.sort()
        uniques = set(nums)
        prevMoveNum = 0

        for i in range(1, length):
            if nums[i] == nums[i - 1]:
                temp = nums[i]
                if prevMoveNum != 0:
                    if temp <= prevMoveNum:
                        moves += prevMoveNum + 1 - temp
                        temp = prevMoveNum + 1
                    else:
                        temp += 1
                        moves += 1
                    while temp in uniques:
                        temp += 1
                        moves += 1
                    uniques.add(temp)
                    prevMoveNum = temp
                else:
                    temp += 1
                    moves += 1
                    while temp in uniques:
                        temp += 1
                        moves += 1
                    uniques.add(temp)
                    prevMoveNum = temp
        return moves

