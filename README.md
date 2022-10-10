# **An analysis on election results for three US counties.**

## Overview of Election Audit
### **Purpose of the audit**
The purpose of this audit was to assist a Colorado board of elections employee in an election audit of the voting results for a U.S. congressional precinct in that state. This audit was performed using **Python** and the goal was to report the following: 
* Total number of votes for each candidate
* Percentage of votes for each candidate
* Winner of the election based on the popular vote
* Total number of votes for each county
* County with the largest turnout

## Election-Audit Results
The results were calculated using different features in Python. The following analysis will provide a more detailed account of the audit process: 

* **Total number of votes for the congressional election**:
The total number of votes for the election was **369, 711**. 

1. This was calculated using a vote counter that established an initial vote count. Then, we used a **for loop**, which helped us iterate through each row in the election_results.csv file, adding a vote for each row in it. The code we used is as follows:

![Total_votes](https://user-images.githubusercontent.com/113153777/194789322-ee73bd10-4660-4755-88b9-9ed5132bbb32.png)

2. After adding a vote for each row in the file, we made sure this information would be stored on a text file and printed on the terminal. For this we used code that incorporated the **"with open"** and **"f string"** functions: 

![total_votesprint](https://user-images.githubusercontent.com/113153777/194789534-2bfcefc6-60d1-4ddb-b5d4-9826dce566d0.png)

* **Breakdown of the number of votes and the percentage of total votes for each county in the precinct:**

The total number and percentage of votes for each county was:
* Jefferson: 10.5% (38,855)
* Denver: 82.8% (306,055)
* Arapahoe: 6.7% (24,801)

1. In order to determine the total number of votes, as well as the percentage of total votes for each county, we first had to establish two things: a list that contained the names of each county and a dictionary that contained each county and their respective vote counts. Thus, we created and empty list and an empty dictionary for this: 

![county_list](https://user-images.githubusercontent.com/113153777/194789767-8f60c364-f0df-4152-9d57-fdcdacdc9b81.png)

2. Then, we used the same for loop we mentioned in the previous section to iterate over every row of the reference file. To get the name of each county, we established the county_name variable:

![county_name](https://user-images.githubusercontent.com/113153777/194789940-1283b228-a7d5-4c94-be6d-2e1ebb25f709.png)

3. We then established a decision statement to make sure that each county's name would only appear once in the county_list list. We used this same decision statement to begin tracking the votes for each county. Then, we added a vote each time the county's name appeared on the list, making sure that this part of the code remained inside the for loop but outside of the decision statement. The code for this whole section is as follows:

![countyname_votes](https://user-images.githubusercontent.com/113153777/194790132-b996a145-1307-4d54-92e3-ab06f099dcaf.png)

4. Finally, we initiated another for loop to be able to determine the total votes and total vote percentage for each county. The county percentage was calculated dividing the number of county votes by the number of total votes and multiplying that by 100. We then printed the county results and saved them to our text file: 

![county_percentage](https://user-images.githubusercontent.com/113153777/194790914-812d60a7-0fbc-4c2c-85d9-d67e431dd2ad.png)

* **County with the largest number of votes**:

The county with the largest number of votes was **Denver**, with **306, 055** votes. 

1. We calculated this, firstly, by establishing two variables that would hold the name and the number of votes for the county with the largest turnout:

![largest_county](https://user-images.githubusercontent.com/113153777/194790723-ca103a45-638a-4b97-b428-daa3adff798b.png)

2. We then used the for loop we used for the previous section, and established a decision statement that would track which county had the largest turnout:

![largest_turnout](https://user-images.githubusercontent.com/113153777/194791127-c016e15b-5929-4818-be9d-37cb2356475e.png)

3. Finally, we printed this data to our terminal and saved it in our text file:

![turnoutsummary](https://user-images.githubusercontent.com/113153777/194791195-7981d9e0-8c9b-45f3-a363-17c70ef49afb.png)

* **Breakdown of the number of votes and the percentage of the total votes each candidate received**:

The results for each candidate were as follows:
* Charles Casper Stockham: 23.0% (85,213)
* Diana DeGette: 73.8% (272,892)
* Raymon Anthony Doane: 3.1% (11,606)

To calculate this information, we followed a very similar process to the analysis we performed for the voting results in each county:

1. We created a list to contain the candidate names, and a dictionary to contain their votes:

![candidate_options](https://user-images.githubusercontent.com/113153777/194791485-ecfcaef9-f10c-4c4a-b158-bd3627d1ddba.png)

2. We used a for loop and a decision statement to retreive their names only once. This same "if" statement was used to track their vote count. As with the county analysis, we used the candidate_votes variable outside of the statement to add the candidate votes:

![candidate_votes](https://user-images.githubusercontent.com/113153777/194791654-12e21886-a042-48f4-b703-d2137798fe5a.png)

3. We used a new for loop to calculate the percentage of votes for each candidate, and then printed the results for each candidate and saved them to the text file:

![eachcandidate](https://user-images.githubusercontent.com/113153777/194791824-361f2de4-34ba-434d-b3fa-6214b13530b5.png)

* **The winning candidate, their vote count, and their percentage of the total votes**:

The winning candidate was **Diana DeGette**, with **272, 892** votes and a voting percentage of **73,8**. The code we used for this section was also very similar to the one we used to determine the county with the largest voting turnout.

1. To determine the winner, we first had to assign three variables that would track their name, their vote count and vote percentage:

![winning_variables](https://user-images.githubusercontent.com/113153777/194792319-f1d32f3d-6dcc-44c0-b039-e33a82d62ca9.png)

2. We used the candidate_votes for loop and a decision statement to track the election winner:

![winnerwinnerchickendinner](https://user-images.githubusercontent.com/113153777/194792467-5a1da88c-08af-44c0-8a63-03b420ca2faa.png)

3. We printed the results to the terminal and saved them to our text file: 

![winner_print](https://user-images.githubusercontent.com/113153777/194792561-35e16c04-86ca-4bf1-b3bc-c51cb8489419.png)

## Election-Audit Summary
Through this analysis it is evident that incorporating the use of a tool such as Python an election analysis is a quick and professional way of getting election results, while ensuring that the results analysis is as rigorous as possible. And, even though the code we worked through is not exactly simple, it has all the potential of being modified and used in further elections. Furthermore, using the same method in further elections would set a precedent in the area that could possibly elevate the voter's trust in the results presented. 

As it is in the interest of the data analysis team responsible for this audit that the commission may use this code in further elections, we propose two simple modifications that would allow this:

1. **Modifying the dataset paths and the text file that contains the results.**

As a new election analysis would certainly require a different dataset to analyze, as well as a new text file to keep the results, the following sections would be modified:

1.1. Path to the dataset: 

1.1.1. Modify "Resources", replace with folder name that contains dataset. 

1.1.2. Modify "election_results.csv" and replace with csv file name.

1.2. Path to text file:

1.2.1. Modify "Analysis" and replace with folder name that will contain new text file
.
1.2.2. Modify "election_analysis.txt" and replace with new text file name. Doing this will create a new text file in case you haven't already done so. Make sure the name ends with "txt". 

![image](https://user-images.githubusercontent.com/113153777/194793340-3ff79a7e-4eee-4f22-9523-14a988a88a14.png)

2. **Modifying the candidate_name and county_name variables**:

It is possible that the dataset you have for a new election analysis is slightly different from the one used for this audit. Although we recommend that the future datasets follow a similar structure to the original one, if they do present variations, we propose the following:

2.1. Modifying the candidate_name and county_name variables:
2.1.1. This would require examining the dataset and determining which column holds the candidate names and county names. Make sure to remember that the first column is referenced with a "0", while our last column would be the total number of columns -1:

![names propo](https://user-images.githubusercontent.com/113153777/194794343-8aa70bb0-790f-4515-8975-0a7ffbdb0158.png)

Do let us know if, in the future, you would be interested in utilizing this method, as we would be delighted to be involved. 



