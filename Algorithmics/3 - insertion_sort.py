# The aim of this code is to sort a table using insertion sort, good for small data sets but bad for a big ones - O(n^2)


def sort_with_insertion(table_to_sort):
    # Outside loop starts from a second element of the table, as we consider it as already sorted
    for outside_loop_count in range(1, len(table_to_sort)):
        # Defining a helping variable that will store a number that we will be shuffling
        number_to_insert = table_to_sort[outside_loop_count]

        # Inside loop will start from the very first number and will execute at least once
        inside_loop_counter = outside_loop_count - 1

        while inside_loop_counter >= 0 and table_to_sort[inside_loop_counter] > number_to_insert:
            # If the number to the left of our number_to_insert is larger then we move it to the right 'making space' for insertion
            table_to_sort[inside_loop_counter + 1] = table_to_sort[inside_loop_counter]
            # decreasing counter as a condition of escaping the loop
            inside_loop_counter -= 1

        # when moving larger number to the right is done we proceed to inserting our number into the table
        table_to_sort[inside_loop_counter + 1] = number_to_insert

    # The table is now sorted so we can return it to main code
    sorted_table = table_to_sort
    return sorted_table


if __name__ == '__main__':
    unsorted_table = [15, 7, 4, 2, 6, 12, 13]
    print('Unsorted table: ' + str(unsorted_table))
    print('After sorting: ' + str(sort_with_insertion(unsorted_table)))
