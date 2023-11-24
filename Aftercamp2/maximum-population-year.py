class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        demography = [0] * 101

        for birth, death in logs:
            demography[birth - 1950] += 1
            demography[death - 1950] -= 1
        
        population = list(accumulate(demography))

        max_popln = max(population)

        for i in range(101):
            if population[i] == max_popln:
                return 1950 + i
        