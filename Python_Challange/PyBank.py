import os
import csv

budget_csv = os.path.join("UR-RICH-DATA-PT-01-2020-U-C","03-Python","HW","Instructions", "PyBank","Resources", "budget_data.csv")
Total_months=[]
Month_Change=0
Net_Change=[]
ChangeList=[]
MonthChangeList=[]
#Net_Total=[]
Net_Total=0
CurrentPL=0
PastPL=0
TotalChange=0
Change=0
count=1
AverageChange=0
CombindList=[]


#Open the cvs file 

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    header = next(csvreader)
    
    for row in csvreader:
        Total_months= sum(1 for row in budget_csv)
        #Net_Total= sum(row[1])
        #sum(row[1])
        #Net_Total = Net_Total+row[1]
        #sum(int(Net_Total))
        Value=float(row[1])
        Net_Total=Net_Total + Value
        #Total_diff=Total_diff-Value
    #Net_Change.append(Value)
        CurrentPL=float(row[1])
        
        if count > 1:
            Change= CurrentPL-PastPL
            TotalChange=TotalChange+Change
            ChangeList.append(Change)
            month=row[0]
            Numtextstring=row[0]+ " " + str(Change)
            MonthChangeList.append(Numtextstring)
            #CombindList=MonthChangeList+ChangeList

            PastPL=CurrentPL
        else:
            PastPL=CurrentPL

        count=count + 1 
    AverageChange=(TotalChange/(Total_months-1))


    
    print("Finacial Analysis")
    print("   ")
    print("-------------------------------------")
    print("Total_Month's = " +str(Total_months))
    print("Total:  " + "$"+str((Net_Total)))
    #print(Avg_Change)
    #print(Net_Change)
    #print(Net_Change)
    #print(TotalChange)
    print("Average Change"+"$"+str((AverageChange)))
    #print(ChangeList)
    #print(MonthChangeList)
    #print(CombindList)
    #print(Numtextstring)
    High=max(ChangeList)
    Low=min(ChangeList)
    position=ChangeList.index(High)
    positionL=ChangeList.index(Low)
    #print(position)
    #print(High)
    #print(Low)
    print("Greatest Increase in Profits:  "+str((MonthChangeList[position])))
    print("Greatest Decrease in Profits: "+ str((MonthChangeList[positionL])))
    #print("Greatest Increase in Profits: " + str(MonthChangeList) + str(max(Changelist)))
    #print(min(BigValue))
    #print(Month_Change)
        #print(row[0])    