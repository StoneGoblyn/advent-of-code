import re

tot_matches = []
pattern = r'mul\(\d+,\d+\)'
regex = re.compile(pattern)

# Read the input file 
with open('input.txt', 'r') as file:
    for line in file:
        matches = re.findall(pattern, line)
        tot_matches.extend(matches)



def parse_matches(matches):
    results = []
    for i, func in enumerate(matches):
        try:
            result = do_maths(func)
            results.append(result)
            print(f"Command {i+1}: {func} = {result}")
        except Exception as e:
            print(f"Error executing command '{func}': {str(e)}")
            results.append(None)
    return results


def do_maths(func):
    try:
        # Split at '(' and remove the trailing ')'
        func_name = func.split('(')[0]
        # Extract just the arguments part and remove the closing parenthesis
        args_str = func.split('(')[1].rstrip(')')
        # Convert string arguments to numbers
        args = [int(arg.strip()) for arg in args_str.split(',')]
        
        result = mul(*args)
        return result
    
    except (IndexError, ValueError) as e:
        raise ValueError(f"Invalid command format: {func}. Error: {str(e)}")
    except KeyError:
        raise NameError(f"Function '{func_name}' not found")
    
def mul(a,b):
    return a*b

answer = sum(parse_matches(tot_matches))
print(answer)