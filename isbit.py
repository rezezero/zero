s = input("Enter string: ")
print("Original String:", s)

and_result = ""
xor_result = ""

for c in s:
    and_result += chr(ord(c) & 127)
    xor_result += chr(ord(c) ^ 127)

print("After AND with 127:", and_result)
print("After XOR with 127:", xor_result)