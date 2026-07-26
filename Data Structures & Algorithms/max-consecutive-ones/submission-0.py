class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0
        curr_count = 0
        for num in nums:
            if num == 1:
                curr_count += 1
            else:
                if max_count < curr_count:
                    max_count = curr_count
                curr_count = 0
        if max_count < curr_count:
                    max_count = curr_count
        return max_count