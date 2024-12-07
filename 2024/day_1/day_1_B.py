

# Read the input file and extract both columns
with open('input.txt', 'r') as file:
    # Split into separate lists for each column
    first_column = [] 
    second_column = [] 
    sim_1_to_2 = []
    sim_1_to_2_score = []
    
    # split out each, remove duplicates
    for line in file:
        first, second = map(int, line.split())
        first_column.append(first)
        second_column.append(second)

# Sort each column independently
sorted_first = sorted(first_column)
sorted_second = sorted(second_column)

# Find similarites from first column in second column
for number in (sorted_first):
    count = sorted_second.count(number)
    sim_1_to_2.append(count) 
    sim_1_to_2_score.append(count * number)
    
tot_score = sum(sim_1_to_2_score)
print(f"Total Score: {tot_score}\n")

print("First\tSimlarity\tScore")
print("-" * 50)  # Separator line

# Output 
for col1, sim, score in zip(sorted_first, sim_1_to_2, sim_1_to_2_score):
    print(f"{col1}\t{sim}\t\t{score}")

# Save to output file
with open('day_1_B_Solution.txt', 'w') as file:
    file.write(f"Total Score: {tot_score}\n")
    file.write(f"First\t\tSimlarity\t\tScore\n")
    file.write("-" * 60 + "\n")
    for col1, sim, score in zip(sorted_first, sim_1_to_2, sim_1_to_2_score):
        file.write(f"{col1}\t\t{sim}\t\t\t\t{score}\n")
