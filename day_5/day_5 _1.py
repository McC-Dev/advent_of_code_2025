from multiprocessing import Pool
import numpy as np

def init_worker(data):
    # declare scope of a new global variable
    global shared_data
    # store argument in the global variable for this process
    shared_data = data


def find_safe_id(check_id: int) -> bool:
    print(check_id)
    for each_safe_range in shared_data:
        start_id = int(each_safe_range.split("-")[0])
        end_id = int(each_safe_range.split("-")[1])
        
        if start_id <= check_id <= end_id:
            return True
        else:
            continue
    
    return False

if __name__ == '__main__':
    with open('day_5/input_1.txt', 'r') as input_file:
        range_list = input_file.read()
        
        safe_ids, check_ids = range_list.split("\n\n")
        
        safe_ids = safe_ids.splitlines()
        check_ids = check_ids.splitlines()
        
        #print(safe_ids, check_ids)

    #safe_ids_set = set()
    ids_to_check = set([int(check) for check in check_ids])
    
#    for id_range in safe_ids:
#        start_id = int(id_range.split("-")[0])
#        end_id = int(id_range.split("-")[1])
        
    with Pool(8, initializer=init_worker,initargs=(safe_ids,)) as pool:
        result = pool.map(find_safe_id, ids_to_check)

    #safe_ids_set = set(result)

    #checked_ids = ids_to_check.intersection(safe_ids_set)
            
    print(f"answer: {sum(result)}")