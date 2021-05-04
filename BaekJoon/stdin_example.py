from sys import stdin

read = stdin.readline

while 1:
    a, b, c = map(int, read().split())
    break


print("{}, {}, {}".format(a, b, c))