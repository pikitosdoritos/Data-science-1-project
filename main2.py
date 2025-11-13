def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list


print('\n' + str(remove_duplicates([1, 2, 1, 3, 2])))