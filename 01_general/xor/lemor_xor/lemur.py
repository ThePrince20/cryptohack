from PIL import Image
from pwn import *


lemur = Image.open("/home/b00129500/cryptohack/cryptohack/01_general/xor/lemor_xor/lemur.png")
flag = Image.open("/home/b00129500/cryptohack/cryptohack/01_general/xor/lemor_xor/flag.png")

xor_images = xor(lemur.tobytes(), flag.tobytes())
images = Image.frombytes(flag.mode, flag.size, xor_images)

images.save('/home/b00129500/cryptohack/cryptohack/01_general/xor/lemor_xor/xor_image.png')