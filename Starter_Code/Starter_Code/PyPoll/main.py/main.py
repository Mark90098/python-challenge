###################################################################################
#this code is for module 3 python challenge part 1. pybank    written by Mark McLaughlin
###################################################################################

#import csv and os libraries to read and navigate csv files on any operating system
import csv
import os

#define varibles
vote_count = 0
votes_can0 = 0
votes_can1 = 0
votes_can2 = 0
votes_can3 = 0

canidate_list = []


#file_path = 'desktop/Starter_Code/Starter_Code/PyBank/Resources/budget_data.csv'
file_path = os.path.join('desktop','Starter_Code','Starter_Code','PyPoll','Resources','election_data.csv')

with open(file_path,'r') as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=",")
    print(csvreader)

    header = next(csvreader)  #skips header in for loop below
    #print(header)

    for row in csvreader:

        if row[2] not in canidate_list: #checks to see if canidate is already in the list. If not it will be added
            canidate_list.append(row[2])
            
        vote_count += 1  #counts total # of rows (votes)

        #canidate_count = canidate_list.count #returns the number of unique canidates

        if row[2] == canidate_list[0]:   #proceeds to count votes of each canidate
            votes_can0 += 1
        elif row[2] == canidate_list[1]:
            votes_can1 += 1
        elif row[2] == canidate_list[2]:
            votes_can2 += 1
        elif row[2] == canidate_list[3]:
            votes_can3 += 1

#def percent(votes_can):


percent0 = '{0:.2f}'.format(votes_can0/vote_count * 100) #calculates % of votes each canidate got. The 1st section specifies 2 decimal places
percent1 = '{0:.2f}'.format(votes_can1/vote_count * 100)
percent2 = '{0:.2f}'.format(votes_can2/vote_count * 100)
#percent3 = '{0:.2f}'.format(votes_can3/vote_count * 100)

percent_list = [percent0,percent1,percent2]
#percent_list = [f'{percent0} & "%",percent1 & "%",f'{percent2} & "%"]

canidate_percent = zip(canidate_list,percent_list) #zip list to display canidates' % votes next to their name
zipped_list = list(canidate_percent)  #need to list it again
print("\n".join(map(str, zipped_list)))  #need this stuff to print each canidate as new line




