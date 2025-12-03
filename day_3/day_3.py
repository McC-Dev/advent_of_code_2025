import numpy as np




number_list = []

def part_one(input_list: list) -> None:
    single_vals = [[int(value) for value in values] for values in input_list]

    value_array = np.array(single_vals)

    shortened_array = np.delete(value_array, -1, axis=1)

    max_rows = np.max(shortened_array, axis=1)
    max_loc = np.argmax(shortened_array, axis=1)

    for row, digit, location in zip(value_array, max_rows, max_loc):
        
        
        shortened_row = row[location+1:]
        second_digit = np.max(shortened_row)
        
        joltage = int(f'{digit}{second_digit}')
        
        print(row, joltage)
        number_list.append(joltage)

if __name__ == '__main__':
    with open('day_3/input_1.txt', 'r') as input_file:
        range_list = input_file.read().splitlines()
        
        single_vals = [[int(value) for value in values] for values in range_list]

        value_array = np.array(single_vals)
        
        a = len(value_array[0])

        
        for row in value_array:
            battery_list = []
            for i in reversed(range(12)):
                
                shortened_array = row[:len(row)-i]
                
                max_value = np.max(shortened_array)
                max_loc = np.argmax(shortened_array)
                
                battery_list.append(str(max_value))
                
                row = row[max_loc+1:]
            
            
            joltage = int("".join(battery_list))
            number_list.append(joltage)

        total = sum(number_list)
        print(f"{total= }")