
from enum import Enum
from itertools import pairwise

# Read the input file 
with open('example.txt', 'r') as file:
    # Split 
    reports = []
   
    # separate reports
    for line in file:
        numbers = list(map(int, line.rstrip().split()))    
        reports.append(numbers)

class Safety_Status(Enum):
    SAFE = 0
    UNSAFE = 1
    
class Problems(Enum):
    NONE = 0
    CHANGE_IN_DIRECTION = 1
    BIG_JUMP = 2
    NO_CHANGE = 3
    
safety = Safety_Status.SAFE
problem_list = []
total_safe_reports = 0
only_up = 0
only_down = 0
problem_tolerance = 1
total_problems = 0
final_list = []


# Check safety levels per report
# Using pairwise to get sequential pairs, check all pair combos if removing one will be ok
for report in reports:
    for first, second in pairwise(report):
        diff = second - first
        if abs(diff) > 3:
            safety = Safety_Status.UNSAFE
            problem_list.append(Problems.BIG_JUMP)
            
        print(f"Between {first} and {second}: Difference = {diff}")
        
        
        
    if (safety.value!= 1):
        total_safe_reports += 1






# for report_index, report in enumerate(reports): 
    # for num_index, num in enumerate(report):
        
    #     if num_index == 0:
    #         prev_num = num
            
    #     if num_index != 0:
    #         level_change = num - prev_num
    #         increasing = level_change > 0
    #         decreasing = level_change < 0
            
    #         if increasing:
    #             only_up = 1
    #         if decreasing:
    #             only_down = 1
    #         prev_num = num
            
    #         if (abs(level_change) > 3):
    #             total_problems += 1
    #             problem_list.append(Problems.BIG_JUMP)
            
    #         if (level_change == 0):
    #             problem_list.append(Problems.NO_CHANGE)
    #             total_problems += 1
                    
    #         if (only_up and only_down):
    #             problem_list.append(Problems.CHANGE_IN_DIRECTION)
    #             total_problems += 1
    #             only_up = 0
    #             only_down = 0
                                     
    #     else:
    #         continue
        
    # if total_problems > 1:
    #     safety = Safety_Status.UNSAFE

    # if (safety.value!= 1):
    #     total_safe_reports += 1
        
    # # if total_problems < 2 and safety.value == 0:
    # final_list.append(f"{report} is {safety._name_}, with {total_problems} problems {[problem.name for problem in problem_list]}")
        
    # # reset for next report
    # safety = Safety_Status.SAFE
    # only_up = 0
    # only_down = 0
    # total_problems = 0
    # problem_list = []
        

print(f"Total Safe Reports: {total_safe_reports}\n")

# Save to output file
with open('day_2_B_Solution.txt', 'w') as file:
    file.write(f"Total Safe Reports: {total_safe_reports}\n")
    file.write("Report\n")
    file.write("-" * 60 + "\n")
    for report_list in (final_list):
        file.write(f"{report_list}\n")
 
