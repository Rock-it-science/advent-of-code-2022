lines = []
with open('input.txt', 'r') as f:
    lines = f.readlines()

max_elf_index = 1 # Elf with max calories
max_elf_cals = 0  # Max elf calories

current_elf_index = 1 # Index of current elf
current_elf_cals = 0 # Number of calories current elf has

for line in lines:
    if line != "\n":
        current_elf_cals += int(line)
    else:
        # End of elf
        if current_elf_cals > max_elf_cals:
            max_elf_cals = current_elf_cals
            max_elf_index = current_elf_index
        current_elf_index += 1
        current_elf_cals = 0

print(f'Elf number {max_elf_index} has the most calories with {max_elf_cals}')
