from DFourth import *
import csv

# -----EXPORTING CSV FILES-----
def write_to_file(filename, data_sample):
    example = csv.write(open(filename, 'w', encoding='utf-8'), dialect='excel')
    example.writerows(data_sample)

write_to_file('_AFI_100/Hero_Villain.csv', AFI_100_Heroes_100_Villains)