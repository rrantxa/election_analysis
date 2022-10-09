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

#Beginning of task 1: Add an accumulator to count the total votes.
total_votes = 0

#Beginning of task 2: Declare a candidate variable.
candidate_options = []

#T3: Create a dictionary to store candidate names and votes.
candidate_votes = {}

#T5: Assign a variable for the winning candidate.
    #Also assign variables to track who wins. 
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file.
with open(file_to_load, "r", encoding = "UTF-8") as election_data:

    #Perform analysis.
    file_reader = csv.reader(election_data)

    #Read header row
    headers = next(file_reader)
    
    #Print each row in the csv file:
    for row in file_reader:
        #T1:Add to the total vote count.
        total_votes += 1

        #T2: Print the candidate name from each row
        candidate_name = row[2]

        #T2: If the candidate does not match any existing candidate:
        if candidate_name not in candidate_options:
            #Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)
        
        #T3: Get a key for each candidate name. 
            #Track each candidate´s vote count.
            #This format means: dictionary_name[key] and then we just get the value.
            candidate_votes[candidate_name] = 0
    #Add a vote to that candidate´s count:
        candidate_votes[candidate_name] += 1
    
    #Save the results to our text file.
    with open (file_to_save,"w", encoding = "Latin1") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")

        print(election_results, end="")

        #Save the final vote count to the text file.
        txt_file.write(election_results)

        #T4: Iterate through the candidate list.
        for candidate_name in candidate_votes:
            #Get vote count for each candidate.
            votes = candidate_votes[candidate_name]

            #Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) *100

            #Get the candidate name, vote count and percentage of votes.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            
            #Print each candidate result to the terminal.
            print(candidate_results)

            #Save the results to the text file.
            txt_file.write(candidate_results)

            #T5: Determine winning vote count and candidate.
            #Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                #If true then set winning count = votes and winning percentage = vote percentage
                winning_count = votes
                winning_percentage = vote_percentage
                #Set the winning candidate = to the candidate´s name
                winning_candidate = candidate_name
            
        #T5: Get the winning candidate. 
        winning_candidate_summary= (
            f"------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"------------------------\n"
            )
        #Print the results to the terminal.
        print(winning_candidate_summary)

        #Save them into the text file.
        txt_file.write(winning_candidate_summary)



    #End of task 1: Print the total votes.
    #print(f"{total_votes:,}")

    #End of T2: Print candidate names.
    #print(candidate_options)

    #T3: Print candidate vote dictionary.
    #print(candidate_votes)


