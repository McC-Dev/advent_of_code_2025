import numpy as np
import csv
import re

regexp =  r" + "


if __name__ == '__main__':
    with open('day_6/input_1.txt', 'r') as input_file:
        input_file_data = input_file.read().splitlines()
        input_clean = [list(data) for data in input_file_data]
        

    numbers = np.array(input_clean[:-1])
    operators = "".join(input_clean[-1]).split()
    
    numbers[numbers == ' '] = '0'
 
    #numbers = numbers.astype(np.int64)
    numbers = np.flip(numbers, axis=1)
  
    
    data_columns = np.transpose(numbers)
    data_columns = np.insert(data_columns, data_columns.shape[0], '0', axis=0)
    
    index = 0
    total = 0
    
    new_column = []
    
    for column in data_columns:
        print(column)
        column_string = "".join(column)

        column = int(column_string)
        if column == 0:
            operator = operators[-1-index]
            #print(new_column, operator)
            new_column = np.array(new_column)
            match operator:
                case "*":
                    total += new_column.prod()
                case "+":
                    total += new_column.sum()
                
            
            
            new_column = []
            index += 1
            continue
        
        elif column_string[-1] == '0':
            column_string = column_string.rstrip("0")
            column = int(column_string)

            
        new_column.append(column)
        
        
        


    print(total)