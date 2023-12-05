#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    j = 0
    if idx >= len(my_list) or idx < 0:
        return new_list
    else:
        for i in new_list:
            if idx == j:
                new_list[j] = element
                return new_list
            j += 1
