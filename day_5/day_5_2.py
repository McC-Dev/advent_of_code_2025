from multiprocessing import Pool
import numpy as np


def day5_solution2(puzzle_ranges):
    solution = 0
    puzzle_ranges = sorted(puzzle_ranges)
    range_temp = puzzle_ranges[0]
    for range in puzzle_ranges[1:]:
        if range[1] <= range_temp[1]:
            pass
        elif range[0] > range_temp[1]:
            solution += 1 + (range_temp[1] - range_temp[0])
            range_temp = range
        elif range[0] <= range_temp[1]:
            range_temp = (range_temp[0], range[1])
    solution += 1 + (range_temp[1] - range_temp[0])
    print("Solution 2: {}".format(solution))
    return solution


if __name__ == '__main__':
    with open('day_5/input_1.txt', 'r') as input_file:
        range_list = input_file.read()
        
        safe_ids = range_list.split("\n\n")[0]
        
        safe_ids = safe_ids.splitlines()
        
        #print(safe_ids, check_ids)
    
    num_safe_ids = [(int(safe.split("-")[0]), int(safe.split("-")[1])) for safe in safe_ids]
    
    
    solution2 = day5_solution2(num_safe_ids)
    