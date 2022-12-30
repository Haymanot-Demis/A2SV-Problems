#time 60
import collections
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        hashT = collections.defaultdict(int)
        for i in range(len(nums)):
            indx = hashT[nums[i]]
            print(indx, i, nums[i] == nums[indx])
            if nums[i] == nums[indx] and indx != i:
                if abs(indx - i) <= k:
                    return True
                else:
                    hashT[nums[i]] = i
            else:
                hashT[nums[i]] = i
        print(hashT)
        return False
               