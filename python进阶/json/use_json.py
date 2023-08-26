import json
content = '''[{"_1":"唐","_2":12},{"_1":"宋","_2":2},{"_1":"元","_2":45}]
[{"_1":"明","_2":2},{"_1":"清","_2":4},{"_1":"夏","_2":5}]
[{"_1":"商","_2":11},{"_1":"周","_2":1},{"_1":"晋","_2":7}]
'''
data = []
content =content.splitlines()
for line in content:
    data.append(json.loads(line))

total = 0
for line in data:
    for dynasty in line:
        total += dynasty['_2']

print(total)