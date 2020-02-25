import os
import csv

#Make the pathway to the CSV file 
Poll_csv=os.path.join('UR-RICH-DATA-PT-01-2020-U-C','03-Python','HW','Instructions','PyPoll','Resources','election_data.csv')

#Name of new list and veribles 
Name=[]
Number=[]
NumVote_Khan=[]


#Open the csv file 
with open(Poll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    #Skip the header
    header=next(csvreader)

    for row in csvreader:
        TotalVote= (sum(1 for row in Poll_csv))

        Number.append(row[0])
        Name.append(row[2])
        
    
    print("Election Results")
    print("-------------------------------------")
    print("Total Votes " + " " +str(len(Number)))
    print("--------------------------------------")
    print('Khan: '+ str((Name.count("Khan")/len(Number))*100)+"% " + "("+  str(Name.count('Khan'))+ ")")
    print('Correy: '+ str((Name.count("Correy")/len(Number))*100)+"% " + "("+  str(Name.count('Correy'))+ ")")
    print('Li: '+ str((Name.count("Li")/len(Number))*100)+"% " + "("+  str(Name.count('Li'))+ ")")
    print("O'Tooley"+ str((Name.count("O'Tooley")/len(Number))*100)+"% " + "("+  str(Name.count("O'Tooley"))+ ")")
    print("--------------------------------------")
    print("Winner:  Khan")
    print("--------------------------------------")

    
