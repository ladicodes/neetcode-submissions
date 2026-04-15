class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = []
        current = []
        mapping = {
            "2": "abc",
            "3":"def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        def backtracking(i=0):
            if len(current) == len(digits):
                res.append("".join(current))
                return
            for c in mapping[digits[i]]:
                current.append(c)
                backtracking(i+1)
                current.pop()
        backtracking()
        return res