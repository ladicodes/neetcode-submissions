class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        map = {}
        for index, number in enumerate(nums):
            diff = target - number
            if diff in map:
                return [map[diff], index]
            map[number] = index
        return