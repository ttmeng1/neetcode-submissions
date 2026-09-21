from collections import Counter
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_counts = Counter(nums)
        for count in num_counts:
            if num_counts[count] != 1:
                return True
        return False
