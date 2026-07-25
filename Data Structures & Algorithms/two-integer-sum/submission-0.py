class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        output = []
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in map:
                output.append(map[complement])
                output.append(i)
                return output
            map[nums[i]] = i
            i += 1