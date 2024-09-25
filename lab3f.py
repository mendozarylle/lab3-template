#!/usr/bin/env python3

"""
Name: Lab3.py
Author: Rylle Mendoza 
Author ID: rmendoza10@myseneca.ca
Date: 2024/sept/25

Usage:

Description:
"""
# Place my_list below this comment (before the function definitions)
my_list = [1, 2, 3, 4, 5]

def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    new_item = ordered_list[-1] + 1  # Get the last item and increment by 1
    ordered_list.append(new_item)  # Append the new item to the list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values found in items_to_remove list from ordered_list
    for item in items_to_remove:
        while item in ordered_list:
            ordered_list.remove(item)  # Remove the item if it exists in the list

# Main code
if __name__ == '__main__':
    print(my_list)                   # Print the initial list
    add_item_to_list(my_list)       # Add items to the list
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)                   # Print the list after additions
    remove_items_from_list(my_list, [1, 5, 6])  # Remove specified items
    print(my_list)                   # Print the final list