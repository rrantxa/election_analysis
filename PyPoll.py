#The data we need to retrieve:
    #1. The total number of votes cast
    #2. A complete list of candidates who received votes
    #3. The percentage of votes each candidate won.
    #4. The total number of votes each candidate won.
    #5. The winner of the election based on popular vote. 

#Step 0.: Creating a path for the csv file. 
#Step 0.1: Dependencies, packages and modules.
#Dependencies are modules and packages, or a programming script that someone else has written, that allows you to increase the functional programming of your code, or speed and efficiency.

# Import the datetime class from the datetime module.
#import datetime as dt

# Use the now() attribute on the datetime class to get the present time.
#now = dt.datetime.now()

# Print the present time.
#print(f"The time right now is  {now}")

import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable to save the file to a path. 
file_to_save = os.path.join("Analysis", "election_analysis.txt")


#Open the election results and read the file.
with open(file_to_load, "r", encoding = "UTF-8") as election_data:

    #Perform analysis.
    file_reader = csv.reader(election_data)

    #Print header row
    headers = next(file_reader)
    print(headers)
    

#Use open() and "w" to write data on the text file. Use with open to open and close. 
with open(file_to_save, "w", encoding = "UTF-8") as txt_file:

    #Write some data on the file.
    txt_file.write("Counties in the election\n-------------------------\nArapahoe\nDenver\nJefferson")


