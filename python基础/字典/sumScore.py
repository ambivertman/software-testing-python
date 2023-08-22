with open("0016_1.txt", 'r', encoding='utf8') as f:
    content = f.readlines()

for index, line in enumerate(content):
    content[index] = line.split()

totalScore = {}
for person in content:
    if person[0][0] not in totalScore:
        totalScore[person[0][0]] = eval(person[1])
    else:
        totalScore[person[0][0]] += eval(person[1])

for key,value in totalScore.items():
    print(f"{key} : {value}")
