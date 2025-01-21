# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Jack Ferland"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101306286"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-14"

#==========================================#
# Place your histogram function after this line


import matplotlib.pyplot as plt


def histogram(graph_list: list[dict], plot_key: str) -> float:
    """
    Create a histogram using the provided data that plots the value of
    the given atribute on the x-axis over 20 intervals from 0 to its maximum 
    value with the exception of occupations, where each inividual occupation 
    is listed. The y-axis is the number of characters who share the same value 
    of an attribute or have the same job. The function returns either -1 if 
    occupation is being sorted or the maximum value for the given attribute.

    >>> histogram([{"Occupation": "AT", "Strength": 3, "Stamina": 5}, {"Occupation": "EB", "Strength": 2, "Stamina": 8}, {"Occupation": "H", "Strength": 1, "Stamina": 3}], "Strength")
    3

    >>> histogram([{"Occupation": "AT", "Strength": 3, "Stamina": 5}, {"Occupation": "EB", "Strength": 2, "Stamina": 8}, {"Occupation": "H", "Strength": 1, "Stamina": 3}], "Stamina")
    8

    >>> histogram([{"Occupation": "AT", "Strength": 3, "Stamina": 5}, {"Occupation": "EB", "Strength": 2, "Stamina": 8}, {"Occupation": "H", "Strength": 1, "Stamina": 3}], "Occupation")
    -1
    """

    data_set = [char[plot_key] for char in graph_list]
    max_val = 0
    fig1 = plt.figure()
    plt.title("Character Data")
    character_set = {}

    if isinstance(data_set[0], str):

        set_values = list(set(data_set))
        length = [data_set.count(value) for value in set_values]
        plt.bar(set_values, length, color="blue")
        plt.xlabel("Occupation")
        plt.ylabel("Number of Characters in Each Occupation")

        plt.show()

        return -1

    else:
        plt.xlabel("Level of " + plot_key)
        plt.ylabel("Number of Characters at a Given Level of " + plot_key)

        for i in range(len(graph_list)):
            if graph_list[i][plot_key] > max_val:
                max_val = graph_list[i][plot_key]

        if max_val >= 20:
            graph_step = max_val / 20
        else:
            graph_step = 1

        for character in graph_list:
            val = character[plot_key]

            if type(val) == int:
                key = f'{plot_key}: {val}'
            elif type(val) == float:
                step = int(val)
                key = f'{plot_key}:{val} - {val + 1}'

            if key in character_set:
                character_set[key] += 1
            else:
                character_set[key] = 1

        keys = list(character_set.keys())
        val = list(character_set.values())

        for k in range(0, int(max_val), int(graph_step)):
            plt.bar([k], [])

        plt.bar(keys, val, color="blue")
        plt.tight_layout()

        plt.show()

        return max_val


# Do NOT include a main script in your submission

