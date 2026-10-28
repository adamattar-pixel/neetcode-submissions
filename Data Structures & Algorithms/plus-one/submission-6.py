class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits) - 1, -1, -1):
            temp = digits[i]
            digits[i] = (digits[i] + carry) % 10
            carry = 1 if temp == 9 and digits[i] == 0 else 0
        if carry == 1:
            return [1] + digits
        return digits