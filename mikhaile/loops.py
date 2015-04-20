import os


def sp():
    print()


def sq(x):
    for n in range(x):
        print('#' * x, end="")
        sp()


def tr(x):
    for n in range(x):
        for m in range(n + 1):
            print('#', end="")
        sp()


def tri(x):
    for n in range(x):
        for m in range(x):
            print('#', end="")
        x -= 1
        sp()


def ar(x):
    if x >= 6:
        for n in range(x):
            for m in range(n - 1 + 1):
                if n < (x / 2):
                    print('#', end="")
            print('#')
    else:
        sq(x)


def main():
    con = 'Y'
    while con == 'Y':
        print('Input value of x = : ', end="")
        a = int(input())
        sq(a)
        sp()
        tr(a)
        sp()
        tri(a)
        sp()
        ar(a)
        print('\nContinue [Y/N] ? : ', end="")
        con = input().upper()
        os.system('clear')

if __name__ == '__main__':
    main()
