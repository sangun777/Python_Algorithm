from sys import stdin

read= stdin.readline

# 빈 딕셔너리 생성
memo = {}

def w(a, b, c):

    # 만약 memo 딕셔너리 안에 입력 a, b, c에 해당하는 키 값이 있으면 반환
    if (a, b, c) in memo:
        return memo[(a, b, c)]

    elif a <= 0 or b <= 0 or c <= 0:
        return 1

    elif a>20 or b>20 or c>20 :
        return w(20, 20, 20)

    elif a < b and b < c:
        # W(~~) 값은 결국에는 재귀를 돌다가 값이 나오게 되는데,
        # 그것을 W_num에 저장하고,
        # memo 딕셔너리 안에 새로운 키 (a, b, c)의 값으로 저장
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

    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))