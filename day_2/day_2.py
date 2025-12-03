import textwrap
from multiprocessing import Pool

def split_int_two(input_string: str) -> tuple[str, str]:
    string_length = len(input_string)
    mid_point = int(string_length/2)

    front = input_string[mid_point:]
    back = input_string[:mid_point]

    return front, back

def part_one(input_list: list) -> None:
    
    number_list = []

    for each_range in range_list:
        start, end = each_range.split('-')

        for value in range(int(start), int(end)+1):
            front, back = split_int_two(str(value))
            
            if front == back:
                #print(value)
                number_list.append(value)

    result = sum(number_list)
    print(result)
        
        
def find_matches(input_string: int) -> int:
    value_string = str(input_string)
    
    for i in range(1, len(value_string)+1):
        options = textwrap.wrap(value_string, i)
        
        if len(options) == 1:
            continue
        
        if len(set(options)) == 1:
            #print(each_range, options, value)
            return input_string
    
    return 0

def part_two(input_list: list) -> None:
    number_list = []

    for each_range in range_list:
        start, end = each_range.split('-')
        with Pool() as p:
            vals = p.map(find_matches, [value for value in range(int(start), int(end)+1)])
            number_list.append(sum(vals))
            print(sum(vals))
                    
    result = sum(number_list)
    print(result)


if __name__ == '__main__':
    with open('day_2/input_1.txt', 'r') as input_file:
        range_list = input_file.read().split(",")
        
    part_two(range_list)



