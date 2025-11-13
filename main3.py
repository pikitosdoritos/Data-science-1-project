def max_in_list(lst):
    max = float('-inf')
    for item in lst:
        if item > max:
            max = item
        
    return max

print('\n' + str(max_in_list([1, 3, 5, 9, 2, 5, 2, 1, 4])))