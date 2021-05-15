answer = 0
prev = ' '
input_string = input()
for i in input_string:
    if i != prev:
      answer += 1
    prev = i
print(answer//2)
