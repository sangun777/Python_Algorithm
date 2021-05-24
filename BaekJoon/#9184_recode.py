from sys import stdin

read = stdin.readline

memo = {}
test_case =[]


def w(a, b, c):
    
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    elif a<=0 or b<=0 or c<=0:
        return 1

    elif a>20 or b>20 or c>20:
        return w(20,20,20)

    elif a<b and b<c:
        w_num = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        memo[(a, b, c)] = w_num
        return w_num

    else:
        w_num = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        memo[(a, b, c)] = w_num
        return w_num

while True:
    a, b, c = map(int, read().split())
    if a==-1 and b==-1 and c==-1:
        break
    test_case.append((a, b, c))

for i in range(len(test_case)):
    w(test_case[i][0], test_case[i][1], test_case[i][2])
    print("w(%d, %d, %d) = %d" % (test_case[i][0], test_case[i][1], test_case[i][2], w(test_case[i][0], test_case[i][1], test_case[i][2])))