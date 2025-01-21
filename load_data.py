# ECOR 1042 Lab 3 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
import string
__author__ = "David Mea Andjou, Isaac Ben-Zvi, Jack Ferland, Alice Hesse"

# Update "" with your team (e.g. T102)
__team__ = "014"


#==========================================#

def character_occupation_list(file_name: str, occupation: str) -> list[dict]:
    """ Returns the list of characters (stored as a dictionary)
    whose occupation is provided as the input parameter

    Precondition: file_name must be 'characters-mat.csv' and occupation a sting

    >>> character_occupation_list ('characters-mat.csv', 'AT')
    [{'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7,
    'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'},
    {another element},
    ]
    >>> character_occupation_list ('characters-mat.csv', 'XXXXX')
    []

    """

    in_file = open(file_name, 'r')
    first_line = True
    dic_list = []
    for line in in_file:
        line = line.strip()
        line = line.split(',')

        if first_line:

            first_line = False
            table_header = line

        else:
            occupation_dic = {}
            occupation_dic[table_header[0]] = str(line[0])
            occupation_dic[table_header[1]] = int(line[1])
            occupation_dic[table_header[2]] = int(line[2])
            occupation_dic[table_header[3]] = int(line[3])
            occupation_dic[table_header[4]] = int(line[4])
            occupation_dic[table_header[5]] = int(line[5])
            occupation_dic[table_header[6]] = float(line[6])
            occupation_dic[table_header[7]] = int(line[7])
            occupation_dic[table_header[8]] = str(line[8])

            if occupation == line[0]:
                occupation_dic.pop('Occupation')

                dic_list.append(occupation_dic)

    in_file.close()

    return dic_list


#==========================================#
def character_strength_list(file_name: str, strength_range: tuple) -> list[dict]:
    """
    Return a list containing an individual dictionary for every
    character whose strength falls within the maximum and minumum
    values of strength_range. If no character falls within this
    range, return an empty list.
    >>> character_strength_list("characters-mat.csv", (10, 11))
    [{'Occupation': 'AT', 'Agility': 8, 'Stamina': 8, 'Personality': 14,
    'Intelligence': 11, 'Luck': 0.61, 'Armor': 10, 'Weapon': 'Club'},
    {'Occupation': 'AT', 'Agility': 8, 'Stamina': 8, 'Personality': 12,
    'Intelligence': 9, 'Luck': 0.44, 'Armor': 10, 'Weapon': 'Dagger'},
    ...
    ]
    >>> character_strength_list("characters-mat.csv", (1, 2))
    []
    >>> character_strength_list("characters-mat.csv", (100, 1000))
    []
    """
    in_file = open(file_name, 'r')
    first_line = True
    character_list = []

    for line in in_file:
        line = line.strip().split(',')

        if first_line:
            first_line = False
            table_header = line
        else:
            if min(strength_range) <= int(line[1]) <= max(strength_range):
                characters = {}
                characters[table_header[0]] = line[0]
                characters[table_header[2]] = int(line[2])
                characters[table_header[3]] = int(line[3])
                characters[table_header[4]] = int(line[4])
                characters[table_header[5]] = int(line[5])
                characters[table_header[6]] = float(line[6])
                characters[table_header[7]] = int(line[7])
                characters[table_header[8]] = str(line[8])

                character_list += [characters]

    in_file.close()
    return character_list


#==========================================#
def character_luck_list(file: str, luck_value: float) -> list[dict]:
    """when given the file name and the luck value returns a dictionary with the descriptors of the sheet for every character with that luck value not including the luck value
    preconditions: luck is a float greater than zero
    >>>character_luck_list('characters-mat.csv',0.5)

    [{'Occupation': 'AT', 'Strength': 12.0, 'Agility': 3.0, 'Stamina': 7.0, 'Personality': 13.0, 'Intelligence': 11.0, 'Armor': 8.0, 'Weapon': 'Staff'}, 

    {'Occupation': 'AT', 'Strength': 13.0, 'Agility': 10.0, 'Stamina': 5.0, 'Personality': 11.0, 'Intelligence': 7.0, 'Armor': 10.0, 'Weapon': 'Club'},
    ...
    ]
    >>>character_luck_list('characters-mat.csv',0.1)
    []
    """
    my_file = open(file, 'r')
    n = 0
    statslist = []
    for line in my_file:
        line = line.strip()
        row = line.split(',')
        if n == 0:
            table_header = row
        elif float(row[6]) < luck_value:
            stats = {}
            stats[table_header[0]] = str(row[0])
            stats[table_header[1]] = float(row[1])
            stats[table_header[2]] = float(row[2])
            stats[table_header[3]] = float(row[3])
            stats[table_header[4]] = float(row[4])
            stats[table_header[5]] = float(row[5])
            stats[table_header[7]] = float(row[7])
            stats[table_header[8]] = str(row[8])
            statslist.append(stats)

        n += 1
    my_file.close()
    return statslist


#==========================================#
# Place your character_weapon_list function after this line


def character_weapon_list(file_name: str, Weapon: str) -> list[dict]:
    """Returning a list of character stats who contain the same weapon specified by the function.

    Precondition: File name must be: "characters-mat.csv". Weapon must be a string

    >>>character_weapon_list("characters-mat.csv", "Club")

    [{'Occupation': 'AT', 'Strength': 14, 'Agility': 2, 'Stamina': 8,
        'Personality': 11, 'Intelligence': 5, 'Luck': 0.78, 'Armor': 8}, ... ]

    >>>character_weapon_list("characters-mat.csv", "Spear")

    [{'Occupation': 'VF', 'Strength': 12, 'Agility': 12, 'Stamina': 10,
        'Personality': 12, 'Intelligence': 8, 'Luck': 0.78, 'Armor': 11}, ... ]

    >>>character_weapon_list("characters-mat.csv", "Staff")

    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6,
        'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8}, ... ]



    """

    in_file = open(file_name, 'r')

    read = True

    dic = []

    for line in in_file:

        line = line.strip()

        line = line.split(',')

        list_ch = {}

        if read:

            table_header = line

            read = False

        else:

            list_ch[table_header[0]] = str(line[0])

            list_ch[table_header[1]] = int(line[1])

            list_ch[table_header[2]] = int(line[2])

            list_ch[table_header[3]] = int(line[3])

            list_ch[table_header[4]] = int(line[4])

            list_ch[table_header[5]] = int(line[5])

            list_ch[table_header[6]] = float(line[6])

            list_ch[table_header[7]] = int(line[7])

            list_ch[table_header[8]] = str(line[8])

            if Weapon == line[8]:

                list_ch.pop("Weapon")

                dic.append(list_ch)

    in_file.close()

    return dic


#==========================================#

# Place your calculate_health function after this line


def calculate_health(file_list: list[dict]) -> list[dict]:
    """Creating a list of character stats along with calculating their health.

    Precondition: File name must be: a list of dictionaries 

    >>>calculate_health([{'Strength': 13, 'Agility': 2, 'Stamina': 6,
 'Personality': 7, 'Intelligence': 8, 'Luck': 0.7,
 'Armor': 8, 'Weapon': 'Staff'}])

    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff', 'health': 80.8}, ...

    ]

    """

    for line in file_list:

        Health = round((line.get('Strength') + line.get('Agility') + line.get('Stamina') + line.get(
            'Personality') + line.get('Intelligence') + (line.get('Armor') ** 2 * line.get('Luck'))), 2)

        line['Health'] = Health

    return file_list


#==========================================#
# Place your load_data function after this line


def load_data(file_name: str, the_filter: tuple) -> list[dict]:
    """ Returns the data that the user wants to load with specified 
    Precondition: 


    >>> load_data('characters-mat.csv', ('Weapon', 'Staff'))

    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 
    'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8},
    {another element},
    …]


    >>> load_data('characters-mat.csv', ('All', -1))

    [{'Occupation': 'AT', 'Strength': 13, 'Agility': 2, 'Stamina': 6, 'Personality': 7, 'Intelligence': 8, 'Luck': 0.67, 'Armor': 8, 'Weapon': 'Staff'}, {another element},...]

    >>> load_data('characters-mat.csv', ('Agilitty', -1))

    []


    """

    pokemon_file = open(file_name, 'r')
    first_line = True
    pokemon_list = []
    a, b = the_filter
    for line in pokemon_file:

        line = line.strip().split(',')

        if first_line:

            first_line = False
            table_header = line

        else:
            if the_filter[0] == ('All'):
                pokemon = {}
                pokemon[table_header[0]] = str(line[0])
                pokemon[table_header[1]] = int(line[1])
                pokemon[table_header[2]] = int(line[2])
                pokemon[table_header[3]] = int(line[3])
                pokemon[table_header[4]] = int(line[4])
                pokemon[table_header[5]] = int(line[5])
                pokemon[table_header[6]] = float(line[6])
                pokemon[table_header[7]] = int(line[7])
                pokemon[table_header[8]] = str(line[8])
                pokemon_list.append(pokemon)

            if the_filter[0] == ('Occupation'):
                return character_occupation_list(file_name, the_filter[1])

            if the_filter[0] == ('Weapon'):
                return character_weapon_list(file_name, the_filter[1])

            if the_filter[0] == ('Strength'):
                return character_strength_list(file_name, the_filter[1])

            if the_filter[0] == ('Luck'):
                return character_luck_list(file_name, the_filter[1])

            if the_filter[0] == ('Health'):
                return calculate_health(the_filter[1])
    pokemon_file.close()
    return pokemon_list


