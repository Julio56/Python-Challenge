
     
import csv

 
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
OTooley_votes = 0
Total_votes = 0
 
 
 

 
with open('election_data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[2]=="Khan":
            Khan_votes+=1
        elif row[2]=="Correy":
            Correy_votes+=1
        elif row[2]=="Li":
            Li_votes+=1
        else:
            OTooley_votes+=1
 
if Khan_votes>Correy_votes and Khan_votes>Li_votes and Khan_votes>OTooley_votes:
    winner="Khan"
elif Correy_votes>Khan_votes and Correy_votes>Li_votes and Correy_votes>OTooley_votes:
    winner="Correy"
elif OTooley_votes>Khan_votes and OTooley_votes>Li_votes and OTooley_votes>Correy_votes:    
    winner="O'Tooley"
else:
    winner="Li"
   
Total_votes = (Khan_votes+Li_votes+OTooley_votes+Correy_votes)
   
 
 
print("")   
print("")   
 
print('Election result' )
print('-------------------------------------------------------------')
print ('Total Votes: ' + str(Total_votes))
  
print('-------------------------------------------------------------')
print("Khan: " + str(round((Khan_votes/Total_votes)*100,3)) +'% '+ '('+str(Khan_votes)+')')
print("Correy: " + str(round((Correy_votes/Total_votes)*100,3)) +'% '+ '('+str(Correy_votes)+')')
print("Li: " + str(round((Li_votes/Total_votes)*100,3)) +'% '+'('+str(Li_votes)+')')
print("O'Tooley: " + str(round((OTooley_votes/Total_votes)*100,3)) +'% '+ '('+str(OTooley_votes)+')')
print('-------------------------------------------------------------')
print('Winner: ' + str(winner) )
print('-------------------------------------------------------------')

f = open("PyPoll.txt", "w")
   

f.write(

'Election result\n'
'-------------------------------------------------------------\n'
'Total Votes: ' + str(Total_votes) + '\n'
'-------------------------------------------------------------\n'
"Khan: " + str(round((Khan_votes/Total_votes)*100,3)) +'% '+ '('+str(Khan_votes)+')' + '\n'
"Correy: " + str(round((Correy_votes/Total_votes)*100,3)) +'% '+ '('+str(Correy_votes)+')' + '\n'
"Li: " + str(round((Li_votes/Total_votes)*100,3)) +'% '+'('+str(Li_votes)+')' + '\n'
"O'Tooley: " + str(round((OTooley_votes/Total_votes)*100,3)) +'% '+ '('+str(OTooley_votes)+')' + '\n'
'-------------------------------------------------------------\n'
'Winner: ' + str(winner)  + '\n'
'-------------------------------------------------------------'




  )
f.close()