import numpy as np
import csv
import re

regexp =  r" + "


if __name__ == '__main__':
    with open('day_6/input_1.txt', 'r') as input_file:
        input_file_data = input_file.read().splitlines()
        input_clean = [data.split() for data in input_file_data]
        
    numbers = np.array(input_clean[:-1], dtype=np.int64)
    operators = input_clean[-1]
    
    total = 0
    for column, operator in zip(np.transpose(numbers), operators):
        match operator:
            case "*":
                total += column.prod()
            case "+":
                total += column.sum()
                
    print(total)