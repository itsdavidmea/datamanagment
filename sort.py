# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "David Mea Andjou, Isaac Ben-Zvi, Jack Ferland, Alice Hesse"

# Update "" with your team (e.g. T102)
__team__ = "014"

#==========================================#
# Place your sort_characters_agility_bubble function after this line


def sort_characters_agility_bubble(given: list[dict], direction: str) -> list:
    """
    Sorting a given list of dictionarys and returning a new list in asending or decending order. 
    Preconditons: given must be a list of dictionaries, and direction must be 'A' for asending or 'D' for decending.

    >>>sort_characters_agility_bubble([{'Occupation': 'AT', 'Strength': 14, 'Agility': 2, 'Stamina': 8, 'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10}, {'Occupation': 'AT', 'Strength': 18, 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11}, {'Occupation': 'AT', 'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 14, 'Intelligence': 11, 'Luck': 0.61, 'Armor': 10}], 'D')

    [{'Occupation': 'AT', 'Strength': 18, 'Agility': 11, 'Stamina': 6, 'Personality': 4, 'Intelligence': 11, 'Luck': 0.83, 'Armor': 11}, {'Occupation': 'AT', 'Strength': 9, 'Agility': 9, 'Stamina': 3, 'Personality': 9, 'Intelligence': 15, 'Luck': 0.5, 'Armor': 10}, {'Occupation': 'AT', 'Strength': 11, 'Agility': 8, 'Stamina': 8, 'Personality': 14, 'Intelligence': 11, 'Luck': 0.61, 'Armor': 10}, {'Occupation': 'AT', 'Strength': 14, 'Agility': 2, 'Stamina': 8, 
    'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8}]

    """

    try:
        if direction == 'D':
            for i in range(len(given) - 1):
                for j in range(len(given) - i - 1):
                    if given[j].get('Agility') < given[j + 1].get('Agility'):
                        given[j], given[j + 1] = given[j + 1], given[j]
        if direction == 'A':
            for i in range(len(given) - 1):
                for j in range(len(given) - i - 1):
                    if given[j].get('Agility') > given[j + 1].get('Agility'):
                        given[j], given[j + 1] = given[j + 1], given[j]
        return given
    except:
        print('Agility missing')
        return given


#==========================================#
# Place your sort_characters_intelligence_selection function after this line

def sort_characters_intelligence_selection(character_data: list[dict], type_sort: str) -> list[dict]:
    """
    Sort a list of dictionaries by the intelligence stat in either descending 
    or ascending order if "D" or "A" are given as the second variable. If the
    intelligence stat is not a key in the dictionary, return the original list
    along with a message stating that intelligience is not in the dictionary.

    sort_intelligence([{"Occupation": "AT", "Intelligence": 7}, 
    {"Occupation": "VF", "Intelligence": 12}], "A")

    >>> [{"Occupation": "AT", "Intelligence": 7}, 
    {"Occupation": "VF", "Intelligence": 12}]

    sort_intelligence([{"Occupation": "HG", "Intelligence": 12}, 
    {"Occupation": "M", "Intelligence": 5}], "D")

    >>> [{"Occupation": "HG", "Intelligence": 12}, 
    {"Occupation": "M", "Intelligence": 5}]

    sort_intelligence([{"Occupation": "HG"}, 
    {"Occupation": "M"}], "A")

    >>> "Intelligence" is not a key in the dictionary
    [{"Occupation": "HG"}, {"Occupation": "M"}]
    """

    min_int = len(character_data)

    try:

        if type_sort == "A":
            for i in range(min_int):
                min_num = i

                for j in range(i + 1, min_int):

                    if character_data[j]["Intelligence"] < character_data[min_num]["Intelligence"]:
                        min_num = j

                character_data[i], character_data[min_num] = character_data[min_num], character_data[i]

        else:
            for i in range(min_int):
                min_num = i

                for j in range(i + 1, min_int):

                    if character_data[j]["Intelligence"] > character_data[min_num]["Intelligence"]:
                        min_num = j

                character_data[i], character_data[min_num] = character_data[min_num], character_data[i]

        return character_data

    except KeyError:
        print("\"Intelligience\" key is not present.")
        return character_data


#==========================================#
# Place your sort_characters_health_insertion function after this line

def sort_characters_health_insertion(list1: list, order: str) -> list:
    """
    when given a list of dictionaries and an order will return a sorted list. sorted by health values in ascending order if order = 'A' and descending order if order = "D". also ensures that the Health key is present in the function.
    preconditions: order is 'A' or 'D'
    >>>sort_characters_health_insertion([{'Health': 24, 'Occupation':'H'},{'Health' : 27, 'Occupation' : 'EB'}],'A')
    [{'Health': 24, 'Occupation': 'H'}, {'Health': 27, 'Occupation': 'EB'}]
    >>>sort_characters_health_insertion([{'Health': 24, 'Occupation':'H'},{'Health' : 27, 'Occupation' : 'EB'}],'D')
    [{'Health': 27, 'Occupation': 'EB'}, {'Health': 24, 'Occupation': 'H'}]
    >>>sort_characters_health_insertion([{"Luck": 0.4, 'Weapon' : 'Staff'},{'Luck':0.3 , 'Weapon': 'Dagger'}], 'D')
    'Health' key invalid
    """
    H = False
    for l in range(0, len(list1)):
        p = 'Health'
        if p in list1[l]:
            H = True
    if H == False:
        print("'Health' key invalid")
        return list1
    elif order == 'A' and H == True:
        for i in range(1, len(list1)):
            Key = list1[i]
            j = i - 1
            while j >= 0 and Key['Health'] < list1[j]['Health']:
                list1[j + 1] = list1[j]
                j -= 1
            list1[j + 1] = Key
        return list1

    elif order == 'D' and H == True:
        for i in range(1, len(list1)):
            Key = list1[i]
            j = i - 1
            while j >= 0 and Key['Health'] > list1[j]['Health']:
                list1[j + 1] = list1[j]
                j -= 1
            list1[j + 1] = Key
        return list1


#==========================================#
# Place your sort_characters_armor_bubble function after this line

def sort_characters_armor_bubble(dic_list: list[dict], sorting_order: str) -> list[dict]:
    """ Returns an ascending or descending list of using the buble sorting system 
    Precondition: Amor should not be in both dictionnaries for the function to displat: "Armor" key is not present  

    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "D")

    [{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}]

    >>>sort_characters_armor_bubble([{'Occupation': 'EB', 'Armor': 11}, {'Occupation': 'H', 'Armor': 10}], "A")

    [{'Occupation': 'EB', 'Armor': 10}, {'Occupation': 'H', 'Armor': 11}]



    >>> sort_characters_armor_bubble([{'Occupation': 'EB'},
    {'Occupation': 'M'}], "D")

    "Armor" key is not present.



    """
    for j in range(len(dic_list) - 1):

        if 'Armor' in dic_list[j].keys():

            if sorting_order == 'A':
                swap = True
                while swap:
                    swap = False
                    for i in range(len(dic_list) - 1):
                        if dic_list[i].get('Armor') > dic_list[i + 1].get('Armor'):

                            aux = dic_list[i]
                            dic_list[i] = dic_list[i + 1]
                            dic_list[i + 1] = aux
                            swap = True

            elif sorting_order == 'D':
                swap = True
                while swap:
                    swap = False
                    for k in range(len(dic_list) - 1):

                        if dic_list[k].get('Armor') < dic_list[k + 1].get('Armor'):

                            aux = dic_list[k]
                            dic_list[k] = dic_list[k + 1]
                            dic_list[k + 1] = aux
                            swap = True

        else:

            print("\"Armor\" key is not present.")

    return dic_list


#==========================================#
# Place your sort function after this line
def sort(dic_list: list[dict], sorting_order: str, attribute: str) -> list[dict]:
    """ Returns a sorted function depending on 4 attributes 
    Precondition: The attributes can to be intelligence, armor, agility or health

    >>> sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "D", "Agility")

    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]


    >>>sort([{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}], "A", "Stamina"))

    Cannot be sorted by " Stamina "

    [{'Occupation': 'EB', 'Agility': 13}, {'Occupation': 'H', 'Agility': 11}]


    """

    if attribute == "Agility":

        return sort_characters_agility_bubble(dic_list, sorting_order)

    elif attribute == "Intelligence":

        return sort_characters_intelligence_selection(dic_list, sorting_order)

    elif attribute == "Health":

        return sort_characters_health_insertion(dic_list, sorting_order)

    elif attribute == "Armor":

        return sort_characters_armor_bubble(dic_list, sorting_order)

    else:

        print("Cannot be sorted by " + attribute)
        return dic_list


# Do NOT include a main script in your submission


