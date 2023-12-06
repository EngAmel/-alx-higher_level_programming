#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return([replace if numb == search else numb for numb in my_list])
