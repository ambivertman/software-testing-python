with open("0016_1.txt", 'r', encoding='utf8') as f:
    content = f.readlines()

for index, line in enumerate(content):
    content[index] = line.split()

Max = 0

for i in range(1, len(content)):
    if content[i][1] > content[i - 1][1]:
        Max = i

print(content[Max][0])
