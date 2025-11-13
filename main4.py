def normalize(lst):
    max_item = max(lst)
    min_item = min(lst)
    new_list = []
    
    for item in lst:
        new_list.append((item - min_item)/(max_item - min_item))
    
    return new_list

print('\n' + str(normalize([1, 5, 9, 10, 3, 4, 9999, 0 ,-4, -10, 2])))