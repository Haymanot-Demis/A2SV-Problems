class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        chemistrySum = 0
        skillSum = skill[0] + skill[-1]
        right  = len(skill) - 1
        for i in range(len(skill)//2):
            if skill[i] + skill[right] == skillSum:
                chemistrySum += skill[i] * skill[right]
                right -= 1
            else:
                return -1
        return chemistrySum

        