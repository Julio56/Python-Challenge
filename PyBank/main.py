import os
import csv

dates = []
value = []

# with open('RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv', 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))



csvpath = os.path.join('..' ,'RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv')
 
with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        print(row)


