with open('../data/raw/advent_2022_1.txt', 'r') as f:
    lines = f.readlines()
    calories = [entry.strip() for entry in lines]

elf_sums = []
current_sum = 0
for entry in calories:
    if entry != '':
        current_sum += int(entry)
    elif entry == '':
        elf_sums.append(current_sum)
        current_sum = 0
elf_sums.append(current_sum)

answer1a = max(elf_sums)

print(answer1a)

elf_sums.sort(reverse = True)
answer1b = elf_sums[0] + elf_sums[1] + elf_sums[2]

print(answer1b)