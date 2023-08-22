def equals(*numset):
    table = {}
    for num in numset:
        if num not in table:
            table[num] = 1
        else:
            table[num] += 1
    for k,v in table.items():
        print(f"数字{k:^3}出现了{v:^3}次")

equals(3, 4, 3, 4, 1, 6, 2)