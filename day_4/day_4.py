import numpy as np

def check_ref(x_coord: int, y_coord: int) -> bool:
    if value_array[y_coord][x_coord] == "@":
        return True
    return False

def check_neighbours(x_coord: int, y_coord: int) -> bool:
    
    north = False if y_coord == 0 else check_ref(x_coord, y_coord-1)    
    north_east = False if any([y_coord == 0, x_coord == (shape[1]-1)]) else check_ref(x_coord+1, y_coord-1)
    east = False if x_coord == (shape[1]-1) else check_ref(x_coord+1, y_coord)
    south_east = False if any([y_coord == (shape[0]-1), x_coord == (shape[1]-1)]) else check_ref(x_coord+1, y_coord+1)
    south = False if y_coord == (shape[0]-1) else check_ref(x_coord, y_coord+1)
    south_west = False if any([y_coord == (shape[0]-1), x_coord == 0]) else check_ref(x_coord-1, y_coord+1)
    west = False if x_coord == 0 else check_ref(x_coord-1, y_coord)
    north_west = False if any([y_coord == 0, x_coord == 0]) else check_ref(x_coord-1, y_coord-1)
    
    if sum([north, north_east, east, south_east, south, south_west, west, north_west]) < 4:
        return True
    
    return False


number_list = []
count = 0
overall = 0

if __name__ == '__main__':
    with open('day_4/input_1.txt', 'r') as input_file:
        range_list = input_file.read().splitlines()
        
    single_vals = [[value for value in values] for values in range_list]

    value_array = np.array(single_vals)
    next_array = value_array
    
    shape = value_array.shape
    
    #loc = value_array[y][x]
    
    while True:
        count = 0
        for y_loc in range(shape[0]):
            for x_loc in range(shape[1]):
                if value_array[y_loc][x_loc] != "@":
                    continue
                
                if check_neighbours(x_loc, y_loc):
                    next_array[y_loc][x_loc] = '.'
                    count += 1
                    

        if count == 0:
            break
        overall = overall + count
        value_array = next_array
    
    
    print(f"{overall= }")
        
        