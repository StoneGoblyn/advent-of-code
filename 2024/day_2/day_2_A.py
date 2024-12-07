
# Read the input file 
with open('input.txt', 'r') as file:
    # Split 
    reports = []
   
    # separate reports
    for line in file:
        numbers = list(map(int, line.rstrip().split()))    
        reports.append(numbers)

safety_status = 0 # 0 = safe
total_safe_reports = 0
only_up = 0
only_down = 0

# Check safety levels per report
for report_index, report in enumerate(reports): 
    for num_index, num in enumerate(report):
        if num_index == 0:
            prev_num = num
        if num_index != 0:
            level_change = num - prev_num
            increasing = level_change > 0
            decreasing = level_change < 0
            if increasing:
                only_up = 1
            if decreasing:
                only_down = 1
            prev_num = num
            if (abs(level_change) > 3) or (level_change == 0) or (only_up and only_down):
                safety_status = 1 # unsafe
        else:
            continue
        
    print(f"{report} is {safety_status} (0 is safe)")

    if safety_status != 1:
        total_safe_reports += 1
    safety_status = 0
    only_up = 0
    only_down = 0
        

print(f"Total Safe Reports: {total_safe_reports}\n")   
 
