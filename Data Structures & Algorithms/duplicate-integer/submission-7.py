class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashet = set()
        for i in nums:
            if i in hashet:
                return True
            hashet.add(i)
        return False
    