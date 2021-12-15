from Crypto.Hash import SHA256
from Crypto.Util.number import *
from Crypto.Cipher import AES

key_length = 128
key = SHA256.new(data=b'5959805911241109643914928800631944794321671043586961836890946136294554770507810148857251869110638484873235200204605081157845088692257708370810040562721345').digest()[:key_length]
iv = bytes.fromhex('334b1ceb2ce0d1bef2af9937cf82aad6')
cipher = AES.new(key, AES.MODE_CBC, iv)
cipher_text = bytes.fromhex('543e29415bdb1f694a705b2532a5beb7ebd7009591503ef3c4fbcebf9e62fe91307e5d98efcd49f9f3b1985956cafc89')
plaintext = cipher.decrypt(cipher_text)
print(plaintext)