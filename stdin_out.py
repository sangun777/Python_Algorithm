import sys

# 백준 BOJ 15552번
# 첫 줄(Test case)은 input으로 받음
T = int(input())

for i in range(T):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)

# # 입력 예시
# 5
# 1 1
# 12 34
# 5 500
# 40 60
# 1000 1000