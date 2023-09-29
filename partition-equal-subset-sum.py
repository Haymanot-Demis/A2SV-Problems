class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = set()
        total = sum(nums)

        if total % 2 == 1:
            return False

        half = total // 2

        for i in range(len(nums)):
            temp = memo.copy()
            temp.add(nums[i])
            for value in memo:
                _sum = value + nums[i]

                if _sum == half:
                    return True
                
                if _sum < half:
                    temp.add(_sum)
            
            if half in temp:
                return True

            memo = temp

        return False