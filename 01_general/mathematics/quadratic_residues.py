ints = [14, 6, 11]
p = 29

for i in range(p):
    if i ** 2 % p in ints:
        print(i)
        break
