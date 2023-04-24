class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            if a + b >= b + a:
                return -1
            return 1

        sorted_nums = sorted(list(map(str, nums)), key=cmp_to_key(compare))
        
        result = int("".join(sorted_nums for sorted_nums in sorted_nums))
        return str(result)