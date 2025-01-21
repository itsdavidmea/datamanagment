# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Alice Hesse"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101314942"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "14"


import numpy as np


def curve_fit(List: list[dict], attribute: str, deg: int) -> str:
    """
    returns the equation of a best fit line for the plot of all different values of a select attribute with their average health value when given a list of dictionaries, the attribute that you're plotting and the degree of the polynomial of the line of best fit.
    preconditions: health and attribute are present in all the dictionaries, and deg is a number greater than zero

    >>>curve_fit([{'Health': 27,'Occupation': 'WA', 'Luck': 0.6},{'Health': 25, 'Occupation':'LA', 'Luck': 0.6},{'Health': 20,'Luck':0.7},{'Health': 24,'Luck':0.8}],'Luck',3)

    'y = 500.0 x^2 + -710.0x + 272.0'


    >>>curve_fit([{'Health': 27,'Occupation': 'WA', 'Luck': 0.4},{'Health': 25, 'Occupation':'LA', 'Luck': 0.5},{'Health': 20,'Luck':0.7},{'Health': 24,'Luck':0.8}],'Luck',3)

    'y = 583.33 x^3 + -950.0 x^2 + 479.17x + -50.0'


    >>>curve_fit([{'Health': 20,'Occupation': 'WA', 'Luck': 0.1},{'Health': 25, 'Occupation':'LA', 'Luck': 0.1},{'Health': 20,'Luck':0.7},{'Health': 0,'Luck':0.7}],'Luck',3)

    'y = -20.83x + 24.58'

    """

    Attribute_list = []
    Health_list = []

    for l in range(0, len(List)):
        if List[l][attribute] not in Attribute_list:
            Attribute_list += [List[l][attribute]]
            Health_list += [[List[l]['Health']]]
        else:
            for i in range(0, len(Attribute_list)):
                if Attribute_list[i] == List[l][attribute]:
                    Health_list[i] += [List[l]['Health']]
    # print(Health_list)
    for k in range(0, len(Attribute_list)):
        health_sum = 0
        for m in range(0, len(Health_list[k])):
            health_sum += Health_list[k][m]
        Health_list[k] = health_sum / (m + 1)

    if len(Attribute_list) > (deg + 1):
        degree = deg
    else:
        degree = len(Attribute_list) - 1

    coefficients = np.polyfit(Attribute_list, Health_list, degree)

    expression = " y = "

    for h in range(0, len(coefficients)):
        if h != (len(coefficients) - 1) and h != (len(coefficients) - 2):
            j = len(coefficients) - 1 - h
            expression += str(round(coefficients[h], 2)) + \
                " x^" + str(j) + str(" + ")
        elif h == (len(coefficients) - 2):
            expression += str(round(coefficients[h], 2)) + "x" + str(" + ")
        else:
            expression += str(round(coefficients[h], 2))
    return expression
