#!/usr/bin/env python3
# Author: asaini85

def create_dictionary(keys, values):
    return dict(zip(keys, values))

def shared_values(dict1, dict2):
    return set(dict1.values()).intersection(set(dict2.values()))

if __name__ == '__main__':
    dict_york = {'Address': '70 The Pond Rd', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M3J3M6', 'Province': 'ON'}
    dict_newnham = {'Address': '1750 Finch Ave E', 'City': 'Toronto', 'Country': 'Canada', 'Postal Code': 'M2J2X5', 'Province': 'ON'}
    
    keys = ['Address', 'City', 'Country', 'Postal Code', 'Province']
    values = ['70 The Pond Rd', 'Toronto', 'Canada', 'M3J3M6', 'ON']
    
    york = create_dictionary(keys, values)
    print('York:', york)
    
    common = shared_values(dict_york, dict_newnham)
    print('Shared Values:', common)
