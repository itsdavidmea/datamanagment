# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "David Mea Andjou"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101297581"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "14"

#==========================================#
# Place your script for your batch_UI after this line


from load_data import*
from sort import*
from curve_fit import*
from histogram import*
import numpy as np


file_name_request = input(
    "Please enter the file where your commands are stored:")
batch_file = open(file_name_request)

for line in batch_file:

    item = line.strip("\n").split(";")
    if item[0].lower() == 'l':
        loaded_dic_list = load_data(item[1], (item[2], item[3]))
        print('Data loaded')

    elif item[0].lower() == 's':
        sorted_data = sort(loaded_dic_list, item[2], item[1])
        if item[-1].lower() == 'n':
            print('You selected not to display the sorted data')

        elif item[-1].lower() == 'y':

            print("Data sorted")
            print(sorted_data)

    elif item[0].lower() == 'c':
        health_dic_list = calculate_health(loaded_dic_list)
        curved_data = curve_fit(health_dic_list, item[1], int(item[2]))
        print("Curve fit with Study time will be shown")
        print(curved_data)

    elif item[0].lower() == 'h':
        hist_graph = histogram(loaded_dic_list, item[1])
        print("Histograms with Study time will be shown")

    elif item[0].lower() == 'e':

        break


batch_file.close()





