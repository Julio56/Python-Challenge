 
import os
import csv
 
profits = 0
Greatest_Increase = 0 
Biggest_Decrease = 0  
Total_Months = []
Total_Profits = []
change = []
dates = []
value = []
 
csvpath = os.path.join('..' ,'RUTJC201904DATA3/hw/week3/Instructions/PyBank/Resources/budget_data.csv')
with open(csvpath, newline='') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
 
  
    highest_value = 0
    next(csv_reader)  
    for row in csv_reader:
      
        dates.append(row[0])
        value.append(int(row[1]))
        profits = int(row[1]) + profits
        
       
Total_Months = len(dates)
Total_Profits = str(profits)
 

<<<<<<< HEAD
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

print(str(len([0])))

=======
 
for i in range(len(value)-1):
    change.append (value[i+1]-value[i])
   
   
Min = min(change)
Max = max(change)
Date_MIN = dates[change.index(Min)+1]
Date_MAX = dates[change.index(Max)+1]
Average_Change = sum(change)/len(change)
 
 
 
 
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(Total_Months))
print("Total: " + str(Total_Profits))
print ("Average Change: " + '$'+str(round(Average_Change,2)))
print("Greatest Increase in Profits: " + Date_MAX + " $"+str(Max))
print("Greatest Decrease in Profits: " + Date_MIN + ' ($'+str(abs(Min))+')' )
 

f = open("main.txt", "w")
	
f.write(
	"Financial Analysis\n"   +
	"Total Months: " + str(Total_Months) + '\n' +
	"Total: " + str(Total_Profits) + '\n' +
	"Average Change: $" +str(round(Average_Change,2)) +'\n'+
	"Greatest Increase in Profits: $" +str(max(value)) +'\n' +
	"Greatest Decrease in Profits: " + '($'+str(abs(Min))+')' 
	)
f.close()         
>>>>>>> 49b0f7c14d7ab432d6123f6ea79e2d8b83fe65af
