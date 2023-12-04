#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    j = 0
    if idx >= len(my_list) or idx < 0:
        return my_list
    else:
        for i in my_list:
            if idx == j:
                my_list[j] = element
                return my_list
            j += 1
