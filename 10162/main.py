time = [300, 60, 10]
answer = []

time_input = int(input())

for t in time:
    answer.append(time_input // t)
    time_input = time_input % t

print(' '.join(map(str, answer)) if time_input == 0 else -1)
