# 25-nest-loop.py


for r in range(1, 11):
    for c in range(1, 11):
        print(r * c, end=' ')
    print()

print()

a = 5
while a > 0:
    b = a
    while b > 0:
        print(a * b, end=' ')
        b -= 1
    print()
    a -= 1

