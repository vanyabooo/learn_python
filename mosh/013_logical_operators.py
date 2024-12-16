has_high_income = True
has_good_credit = True

if has_high_income and has_good_credit:
    print("Eligible for loan")

# AND == both
# OR == at least one
# XOR == at least one but not both

# NOT == opposite

# AND == both
# OR == at least one
# XOR == at least one but not both

# NOT == opposite

# bitwise operators

# bitwise AND
a = 5  # 0b0101
b = 3  # 0b0011
print(a & b)  # 0b0001 -> 1

# bitwise OR
a = 5  # 0b0101
b = 3  # 0b0011
print(a | b)  # 0b0111 -> 7

# bitwise XOR
a = 5  # 0b0101
b = 3  # 0b0011
print(a ^ b)  # 0b0110 -> 6

# bitwise NOT
a = 5  # 0b0101
print(~a)  # 0b1010 -> -6

# bitwise LS (left shift)
a = 5  # 0b0101
print(a << 1)  # 0b1010 -> 10
print(a << 2)  # 0b10100 -> 20

# bitwise RS (right shift)
a = 5  # 0b0101
print(a >> 1)  # 0b0010 -> 2
print(a >> 2)  # 0b0001 -> 1

