# Given a signed 32 - bit integer x,
# return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range[-231, 231 - 1], then return 0.

# Assume the environment does not allow you to store  64 - bit  integers(signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1


def reverse(self, x: int) -> int:
    negative_flag = False
    rev_num = 0
    if x < 0:
        x = -1 * x
        negative_flag = True

    while x != 0:
        remainder = x % 10
        rev_num = rev_num + (10 ** (len(str(x)) - 1)) * remainder
        x = x // 10

    if negative_flag == True:
        rev_num = -1 * rev_num

    if rev_num > (2 ** 31) - 1 or rev_num < -2 ** 31:
        return 0

    return rev_num