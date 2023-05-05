class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subsequences = [[nums[0]]]
        for num in nums[1:]:
            found = False
            for i in range(len(subsequences) - 1, -1, -1):
                if subsequences[i][-1] == num - 1:
                    subsequences[i].append(num)
                    found = True
                    break

            if not found:
                subsequences.append([num])

        for i in range(len(subsequences) - 1, -1, -1):
            if len(subsequences[i]) < 3:
                return False
        return True