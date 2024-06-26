import csv
from random import *

'''
This script is used to generate a csv file with random data for the healthData.csv file.

Suggestions Key:
    0. No suggestion
    1. Cut calories
    2. Excerise more
    3. Walk more
Dislikes Key:
    0. No dislike
    1. Fasting
    2. Excerise
    3. Walking
'''

# Rowan do rows 1-250

with open('healthData.csv', 'w') as file:
    writer = csv.writer(file)

    data = []
    
    for rows in range(0,501):
        if(rows == 0):
            data = [
                'User Number',
                'Day Number',
                'Calories Intake',
                'Calories Burned',
                'Sex',
                'Weight',
                'Target Weight',
                'Steps Taken',
                'Suggestion',
                'Dislike'
            ]
            # User Number ,Day Number ,Calories Intake ,Calories Burned ,Sex ,Weight ,Target Weight ,Steps Taken ,Suggestion ,Dislike

        else:
            if (randint(0, 1) == 0):
                data = [
                    rows,
                    randint(0, 50),
                    randint(2500, 3000), 
                    randint(2000, 2450), 
                    'M', 
                    randint(197-25, 197+25), 
                    150, 
                    randint(500, 15000), 
                    0,
                    randint(0, 3)
                ]
            else:
                data = [
                    rows,
                    randint(0, 50),
                    randint(1600, 2000), 
                    randint(1600, 1950), 
                    'F', 
                    randint(171-25, 171+25), 
                    125, 
                    randint(500, 15000), 
                    0,
                    randint(0, 3)
                ]
        
        #get the header of a csv file and write it to the file

        writer.writerow(data)