class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(num) for num in digits]
        digit = int("".join(digits))
        digit = str(digit+1)
        ans = [int(num) for num in digit]
        return ans