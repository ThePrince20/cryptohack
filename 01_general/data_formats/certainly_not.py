from Crypto.PublicKey import RSA


rsa_key = RSA.import_key(open('/home/b00129500/cryptohack/cryptohack/01_general/data_formats/2048b-rsa-example-cert.der', 'rb').read())

print(rsa_key.n)
