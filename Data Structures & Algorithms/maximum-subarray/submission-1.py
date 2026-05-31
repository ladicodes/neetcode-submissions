class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsub = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            maxsub = max(maxsub, current_sum)
        return maxsub