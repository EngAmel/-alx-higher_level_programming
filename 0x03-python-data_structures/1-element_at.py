#!/usr/bin/python3
def element_at(my_list, idx):
    j = 0
    if idx > len(my_list) or idx < 0:
        return None
    else:
        for i in my_list:
            if idx == j:
                return my_list[j]
            j += 1
