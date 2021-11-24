from sys import stdin

print('내용을 입력하세요 :', end = ' ')

s = stdin.readline().rstrip()

print('입력한 내용은 %s 입니다.' %s)
print('입력한 내용의 길이는 %d 입니다.' %len(s))