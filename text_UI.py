# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Isaac Ben-Zvi"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101293061"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-14"

#==========================================#
# Place your script for your text_UI after this line
import time
import load_data
import string
import sort
import curve_fit
import histogram
a = True
while a:
    user_input = input(
        'The available commands are:\nL)oad Data\nS)ort Data\nC)urve Fit\nH)istogram\nE)xit \n\nPlease type your Command:')
    user_input = user_input.upper()
    if user_input == 'L':
        # characters-mat.csv
        user_file = input('Please enter the name of the file:')
        user_filter = input('Please enter the attribute to use as a filter:')
        user_attribute = input('Please enter the value of the attribute:')
        try:
            loaded_list = load_data.load_data(
                user_file, (user_filter, eval(user_attribute)))
            print('data loaded')
        except:
            loaded_list = load_data.load_data(
                user_file, (user_filter, user_attribute))
            print('data loaded')

    elif user_input == 'S':
        user_attribute = input(
            'Please enter the attribute you want to use for sorting:')
        user_direction = input('Ascending (A) or Descending (D) order:')
        user_direction = user_direction.upper()
        try:
            sort.sort(loaded_list, user_direction, user_attribute)
        except:
            print('File not loaded. Please, load a file first.')
            continue
        userWill = input(
            'Data Sorted. Do you want to display the data?(Y/N):')
        userWill = userWill.upper()
        if userWill == 'Y':
            print(loaded_list)
        if userWill == 'N':
            print('ok')

    elif user_input == 'C':
        userAttribute = input(
            'Please enter the attribute you want to use to find the best fit for Health:')
        userPoly = input(
            'Please enter the order of the polynomial to be fitted:')
        deg = int(userPoly)
        load_data.calculate_health(loaded_list)
        try:
            print(curve_fit.curve_fit(loaded_list, userAttribute, deg))
        except:
            print('Data not loaded')
    elif user_input == 'H':
        userAttribute = input(
            'Please enter the attribute you want to use for plotting:')
        histogram.histogram(loaded_list, userAttribute)
    elif user_input == 'E':
        print('Exited')
        break

    else:
        print('invalid command')

#============================================================================#
