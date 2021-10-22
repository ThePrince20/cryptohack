string = "label"

# XOR against each ordinal repr of each character in string
result = [(ord(c) ^ 13) for c in string]

# Convert ordinal repr into ASCII string
flag = ''.join([chr(x) for x in result])


print(flag)