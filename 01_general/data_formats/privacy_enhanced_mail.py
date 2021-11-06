from Crypto.PublicKey import RSA


rsa_key = RSA.import_key(open('/home/b00129500/cryptohack/cryptohack/01_general/data_formats/transparency.pem', 'rb').read())

print(rsa_key.n)
