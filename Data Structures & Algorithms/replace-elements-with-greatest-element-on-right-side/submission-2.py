class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        i = len(arr) - 1
        max_num = -1
        ans = [0] * (i + 1)
        while i >= 0:
            ans[i] = max_num
            max_num = max(arr[i], max_num)
            i -= 1
        return ans
                
            