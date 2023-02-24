class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        """
        the problem says that when we go through the array if the comparison sign previous numbers was greater or less than the comparison of the current two number must be the reverse sign of that if not we save the maximum length
        """
        length = len(arr)
        if length == 1:
            return 1
        left = 0
        right = 1
        flag = None
        max_turbulent_size = 0
        if arr[0] > arr[1]:
            flag = True
        elif arr[0] < arr[1]:
            flag = False
        else:
            left = 1
        
        while right < length - 1:
            if flag == True and arr[right] < arr[right + 1]:
                right += 1
                flag = False
            elif flag == False and arr[right] > arr[right + 1]:
                right += 1
                flag = True
            else:
                max_turbulent_size = max(max_turbulent_size, right - left + 1)
                left = right
                if arr[right] > arr[right + 1]:
                    flag = True
                elif arr[right] < arr[right + 1]:
                    flag = False
                else:
                    flag = None
                    left += 1
                right += 1
        max_turbulent_size = max(max_turbulent_size, right - left + 1)
        return max_turbulent_size