from BSecond import *
def create_bool_field_from_search_term(data_sample, search_term):
    new_array = []
    new_array.append(data_sample[0].append(search_term))

    for row in data_sample[1:]:
        new_bool_field = False
        if search_term in row[7]:
            new_bool_field = True

        row.append(new_bool_field)
        new_array.append(row)

    return new_array

def filter_col_by_bool(data_sample, col):
    matches_search_term = []

    for item in data_sample[1:]:
        if item[col]:
            matches_search_term.append(item)
    return matches_search_term

# -----BELOW: PRINTS OUT THE CSV AS ONE LONG STRING, WITH T/F BOOL VALUES ADDED AT THE END-----
my_new_csv = create_bool_field_from_search_term(data_from_csv, 'F')
print('This is the entire CSV in one array: {}'.format(my_new_csv))

all_csv = filter_col_by_bool(my_new_csv, 8)
print('The entire CSV in one array: {}'.format(all_csv))