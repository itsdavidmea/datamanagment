#  Project Title: Sortify: Precision sorting for better data analysis

### Date:
09/04/2024

### Software’s Name and version:
SortifyOS 10.0

### Contact Information:
David Mea Andjou  
davidmeaandjou@cmail.carleton.ca 

## Description:
Our software is built to load and manipulate the data given into more easily readable forms and to calculate additional attributes based on the previously given data. Our software is also able to find lines of best fit and make histograms based on data given. 

## Dependencies: 
To use this program you need to have Python installed we used Python 3.11, you also need to install the Numpy and matplotlib modules before use. You also need to have the check module. Along with an IDE of your choice we also need csv. 

## Installation:

In order to run the software provided, run the command: 

py –m pip install “Sortify” 


## Usage:
### Text UI:

Open the text UI

Run the program

You will be shown a prompt to chose which command you want to run

```
The available commands are:
L)oad Data
S)ort Data
C)urve Fit
H)istogram
E)xit

Please type your Command:
```

If at any point you chose E it will exit you out of the program

If you chose S, C, or H then you will get an error message
- you are then given the chance to select a command again with the same choices as before

If you chose L then you will be prompted to enter the name of the file you would like to load

After entering the file name you are prompted to enter the name of the attribute you will use to filter it.

If you select S then you will be prompted to enter the attribute that you will be sorting by
- you will then be asked to enter the order in which you would like to sort it be that ascending (A) or descending (D)

- This will then print out the list of dictionaries sorted by your inputs 
- Then you will get shown once again the menu where you can pick a command

If you chose C then you will be prompted to enter the name of the attribute you want to use to find the line of best fit
 - You will then be prompted to chose the degree of the polynomial to which you want your line of best fit
 - Then the equation for the line of best fit will be printed and the command menu will reappear
 

If you select H then you will be prompted to enter the name of the attribute you want to use to plot the histogram
- The histogram will then be prited and the command menu will appear once again
 
### Batch UI:

The Batch UI is run in a very similar way to the Text UI but there is a difference in the way that the Values are inputted. 
In the Batch UI the inputs are entered in the format on a .txt file 

First_Input; Last_input; ... ;Last_Input

where you put the inputs in the order that they will be asked in, and each value is separated by a semicolon.

## Credits:
**Alice Hesse**
- character_luck_list 
- test_return_list 
- sort_characters_health_insertion 
- curve_fit 


**David Mea Andjou**
- character_occupation_list 
- test_return_correct_dict_inside_list 
- sort 
- user manual for the batch UI 
- batch UI 
- Helped with README file

**Isaac Ben-Zvi** 

- test_calculate_health
- sort_characters_agility_bubble 
- user manual video for the text UI  
- calculate_health 
- Text UI 

**Jack Ferland** 

- character_strength_list 
- test_return_list_correct_length 
- Sort_characters_intelligence_selection 
- histogram 

License:
MIT License

Copyright (c) 2024 Sortify

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.