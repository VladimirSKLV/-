f1 = 1
f2 = 1

n = int(input())

print(f1, f2, end =' ')
while n > 0:
    f1, f2 = f2, f1 + f2
    print(f2, end = ' ')
    n -= 1