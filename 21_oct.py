def smaller(lists):
    # Start with the first list as the smallest
    smallest_list = lists[0]

    # Iterate through each list
    for lst in lists:
        # If a smaller list is found, update smallest_list
        if len(lst) < len(smallest_list):
            smallest_list = lst

    return smallest_list

# Test cases
print(smaller([[-2, -1, 0, 0.12, 1, 2], [3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
# Output: [3, 4, 5]

print(smaller([[-2, -1, 0, 0.12, 1, 2], ['a', 'b', 'c', 'd', 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]]))
# Output: [6, 7, 8, 9, 10]

