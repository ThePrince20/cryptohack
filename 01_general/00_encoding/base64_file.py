# Imports base64
import base64

# String of hex
hex_string = '72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf'

# Converts hex_string to hex
hex = bytes.fromhex(hex_string)

# print(type(hex))

# Encodes and Prints hex converted to base64
print(base64.b64encode(hex))
