class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        max_num = -1
        while i >= 0:
            temp = arr[i]
            arr[i] = max_num
            max_num = max(temp, max_num)
            i -= 1
        return arr
                
            