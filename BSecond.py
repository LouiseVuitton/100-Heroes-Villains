from AFirst import *

def number_of_records(data_sample):
    return len(data_sample)

number_of_characters = number_of_records (data_from_csv)

print(number_of_characters, 'characters in our data sample')
print('There are {} characters in our data sample.'.format(number_of_characters))

# def number_of_records2(data_sample):
#     return data_sample.size
#
# number_of_characters_my_csv = number_of_records2(my_csv)
# print(number_of_characters_my_csv, 'characters in our data sample')