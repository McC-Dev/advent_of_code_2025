'''This module contains functions to solve Day 1 challenges.'''


dial_location = 50
count = 0

with open('day_1/input_1.txt', 'r') as input_file:
    instructions = input_file.read().splitlines()
    
    
for instruction in instructions:
    direction = instruction[0]
    
    distance = instruction[1:]
    
    if direction == "R":
        for i in range(int(distance)):
            dial_location += 1
            if dial_location == 100:
                dial_location = 0
                count += 1
            
            
    elif direction == "L":
        for i in range(int(distance)):
            dial_location -= 1
            if dial_location == 0:
                count += 1
            elif dial_location == -1:
                dial_location = 99

            

print(dial_location)
print(count)