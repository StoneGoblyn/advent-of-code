

# Read the input file and extract both columns
with open('input.txt', 'r') as file:
    # Split into separate lists for each column
    first_column = [] 
    second_column = [] 
    distance = []
    
    # split out each, remove duplicates
    for line in file:
        first, second = map(int, line.split())
        first_column.append(first)
        second_column.append(second)

# Sort each column independently
sorted_first = sorted(first_column)
sorted_second = sorted(second_column)

# Find difference between column 1 and column 2
for sort1, sort2 in zip(sorted_first, sorted_second):
    diff = sort1 - sort2
    distance.append(abs(diff))
    
tot_distance = sum(distance)

print(f"Total Distance: {tot_distance}\n")

# Print both sorted columns side by side
print("First\t\tSecond\t\tDistance")
print("-" * 60)  # Separator line

# Output the sorted columns
for num1, num2, dist in zip(sorted_first, sorted_second, distance):
    print(f"{num1}\t\t{num2}\t\t{dist}")

# Save to output file
with open('total_distance.txt', 'w') as file:
    file.write(f"Total Distance: {tot_distance}\n")
    file.write("First\t\tSecond\t\tDistance\n")
    file.write("-" * 60 + "\n")
    for num1, num2, dist in zip(sorted_first, sorted_second, distance):
        file.write(f"{num1}\t\t{num2}\t\t{dist}\n")
