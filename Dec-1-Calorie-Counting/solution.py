lines = []
with open('Dec-1-Calorie-Counting/input.txt', 'r') as f:
    lines = f.readlines()

all_elf_cals = [] # List of all elf calorie numbers for pt. 2

max_elf_index = 1 # Elf with max calories
max_elf_cals = 0  # Max elf calories

current_elf_index = 1 # Index of current elf
current_elf_cals = 0 # Number of calories current elf has

for line in lines:
    if line != "\n":
        current_elf_cals += int(line)
    else:
        # End of elf
        all_elf_cals.append(current_elf_cals)
        if current_elf_cals > max_elf_cals:
            max_elf_cals = current_elf_cals
            max_elf_index = current_elf_index
        current_elf_index += 1
        current_elf_cals = 0

print(f'Elf number {max_elf_index} has the most calories with {max_elf_cals}')

# Part 2: Compute top 3 elf calories total
all_elf_cals.sort(reverse=True)
top_3_cals_total = all_elf_cals[0] + all_elf_cals[1] + all_elf_cals[2]
print(f'The top 3 elves are carrying {top_3_cals_total} calories')
