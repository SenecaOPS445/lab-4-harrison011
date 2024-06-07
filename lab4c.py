#!/usr/bin/env python3
#Author: Harrison Iruthayathas
#Author ID: hiruthayathas

# Dictionaries
dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
# Lists
list_keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
list_values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']

def create_dictionary(keys, values):
    # Place code here - refer to function specifics in section below
    new_dict = {}
    counter = 0
    for itemk in keys:
        new_dict[itemk] = values[counter]
        counter+= 1
    return new_dict

def shared_values(dict1, dict2):
    # Place code here - refer to function specifics in section below
    dict1_values = list(dict1.values())
    dict2_values = list(dict2.values())
    shared_values = []
    for item in dict1_values:
        for item2 in dict2_values:
            if item == item2 and item not in shared_values:
                shared_values.append(item)
    return set(shared_values)


if __name__ == '__main__':
    york = create_dictionary(list_keys, list_values)
    print('York: ', york)
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values', common)