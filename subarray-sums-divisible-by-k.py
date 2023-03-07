class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        It is amazing to know that the in order to the difference between two number is to be divisble b an other number, each of then must have the same remainder when disible by the divisor  lonely. build the prefix sum then chekc is the current sum can be divisible by the given k or if there is a prefix sum with the same remainder in the hashTable. Each time save the modulo of the prefixSum in the hashTable. 
        """
        hashMap = defaultdict(lambda: 0) # will return 0 if not exist
        hashMap[0] = 1
        count = 0
        if nums[0] % k == 0:
            count += 1
        hashMap[nums[0] % k] += 1
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
            count += hashMap[nums[i] % k]
            hashMap[nums[i] % k] = hashMap.get(nums[i] % k, 0) + 1
      
        return count