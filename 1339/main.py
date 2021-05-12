import re

a = ['%8s' % input() for _ in range(int(input()))]

dic = {}
for i in range(8):
    for j in range(len(a)):
        if a[j][i] != ' ':
            if not dic.get(a[j][i]):
                dic[a[j][i]] = 0
            dic[a[j][i]] += 10 ** (7 - i)

dic_sort = sorted(dic, key=lambda x: dic[x], reverse=True)

num = 9
for i in dic_sort:
    dic[i] = num
    num -= 1

answer = 0
for i in a:
    text = ""
    for j in re.findall("[A-Z]", i):
        text += str(dic[j])
    answer += int(text)
print(answer)
