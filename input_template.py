from sys import stdin

print("숫자를 입력하세요 : ")

# s = stdin.readline().rstrip()

# print("출력 : ", s)
# print(type(s))

# a = stdin.readline().split()
# print("출력 : ", a)
# print(type(a))

b = list(map(int, stdin.readline().split()))
print("입력한 숫자는 : ", b)  # 문자열을 요소로 하는 리스트 형태로 출력됨
print(type(b))
for i in b:
    print(type(i))