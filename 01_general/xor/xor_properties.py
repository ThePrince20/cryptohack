def xor_bytes(b1, b2):
    return bytes(a ^ b for (a, b) in zip(b1, b2))

key1 = bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')

# KEY2 ^ KEY1
k2_xor_k1 = bytes.fromhex('37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e')
key2 = xor_bytes(k2_xor_k1, key1)

# KEY2 ^ KEY3
k2_xor_k3 = bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
key3 = xor_bytes(k2_xor_k3, key2)

# FLAG ^ KEY1 ^ KEY3 ^ KEY2
flag = bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
flag = xor_bytes(flag, key1)
flag = xor_bytes(flag, key2)
flag = xor_bytes(flag, key3)

print(flag)