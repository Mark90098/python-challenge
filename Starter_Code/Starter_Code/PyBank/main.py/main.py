###################################################################################
#this code is for module 3 python challenge part 1. pybank    written by Mark McLaughlin
###################################################################################

#define varibles
count = 0
total_losses_gains = 0
prev_row = 1088983 #1st value in csv so 1st change = 0
prev_change = 0
max_profit_decrease = 0
max_profit_increase = 0
total_change = 0


#import csv and os libraries to read and navigate csv files on any operating system
import csv
import os

#file_path = 'desktop/Starter_Code/Starter_Code/PyBank/Resources/budget_data.csv'
file_path = os.path.join('..','Resources','budget_data.csv')

with open(file_path,'r') as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=",")
    print(csvreader)

#read header in 1st row and skip this line for later for loop. Do nothing if theres no header
    header = next(csvreader)
    #print(header)     #dont need to print this

    for row in csvreader:
        ######################################## dont need these if statements. line 27 skips header already ##############################################
        #if isinstance(row[1],str) == True:  #trying to eliminate the 1st title row but all data types are string.
        #need to convert everything except 1st title row to integer
        #if int(row[1]) == row[1]:  # if data can't be made into an integer, this if statement won't trigger (1st row)
        #if row[1] != "Profit/Losses":  #can't figure out how to turn values into integers so this will do
        #################################################################################################################

        
        count += 1  #counts the # of rows (months)
        total_losses_gains += int(row[1])  #adds this month's gain or loss to total gain/loss
        change = int(row[1]) - prev_row
        total_change += change
            
        
        if change > max_profit_increase:  #find max profit increase
            max_profit_increase = change
            increase_date = row[0]
        if change < max_profit_decrease:  #find max profit decrease
            max_profit_decrease = change
            decrease_date = row[0]

        prev_row = int(row[1])  #final lines are to set current values to previous values
        prev_change = change

avg_change = '{0:.2f}'.format(total_change/(count-1))  #this should be outside of the for loop to output a single number, the final number. Format to 2 decimals It is count - 1 because there is 1 less change than there are data points

#print out all desired values. 
print('Financial Analysis \n----------------------------- \n') #\n makes new line
print('Total months:',count)
print('Total gain/losses: $',total_losses_gains)
print('Average change:', avg_change)
print('Max profit increase:', increase_date, '  $', max_profit_increase)
print('Max profit decrease:', decrease_date, '  $', max_profit_decrease)

dir_path = os.path.dirname(os.path.realpath("main.py"))

#export results into csv fil
with open(os.path.join(dir_path, "results.csv"),"w") as export_file:
    writer = csv.writer(export_file)
    writer.writerow(avg_change)   