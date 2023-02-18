class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        hashTable = set()
        for interval in ranges:
            for num in range(interval[0], interval[1] + 1):
                hashTable.add(num)
        
        for x in range(left, right + 1):
            if x not in hashTable:
                return False
        
        return True
        