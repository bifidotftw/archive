'''
Read csv file, put dates into list
Go through every element in list and convert it into full date
    Handled differently for 3 and 4 digit dates
Write to csv
'''
import csv

data = [] # Initiate variable as list for appending values in for loop
with open('dates.csv', newline='') as inputfile: # Read csv file line by line
    for row in csv.reader(inputfile): # Add each line as element in list
        data.append(row[0])

date_list = [] # Initiate variable as list for appending modified values in for loop
for i in data:
    if len(i) == 3: # If date has 3 digits
        date = '0'+i[0]+ '.' + i[1:3] + '.' +'2020'
        date_list.append(date)
    if len(i) == 4: # If date has 4 digits
        date = i[0:2]+ '.' + i[2:4] + '.' +'2020'
        date_list.append(date)

# Write to csv
with open('dates_formatted.csv', 'w', newline='') as myfile:
    wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
    for i in date_list: # Write each element into its own column
            wr.writerow([i])
