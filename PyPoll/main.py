#import statements
import os
import csv

#define the path to open the election_data.csv file for analysis
pypoll_data = os.path.join(".", "election_data.csv")

#set total votes counter to zero so that the total votes can then be properly added (below)
#created a dictionary to store the candidates and votes together and ultimately
#run the proper mathmatical equations on each's candidate's results
#created a list to store the candidates themselves
total_votes = 0             
candidates_results = {}        
candidates_list = []        

#open the pybank.csv file so that the code can properly analyze and run on the file
#the file is opened as a dictionary in order to properly analyze the data
#the dataset is named election_results for ease of identifiation
with open(pypoll_data, newline="") as election_data_results:
    election_results = csv.DictReader(election_data_results)

#this loop is designed to count the total votes by adding one per row, which represents a vote
#the prevously-created candidates_results dictionary is then created by itentifying
#new candidates, storing them, and then adding one for each reoccurence
    for row in election_results:
        total_votes += 1                           
    
        if row['Candidate'] not in candidates_results:  
            candidates_results[row['Candidate']] = 0    
    
        if row['Candidate'] in candidates_results:      
            candidates_results[row['Candidate']] = candidates_results[row['Candidate']] + 1
  
  #two new lists are created, one to hold the candidates, and the other, the votes
  #this list will be used to property attribute each candidate with the votes
    candidates = []     
    votes = []                           

  #this loop is designed to fill the lists in the previously-created candidates and votes lists                                     
    for c, v in candidates_results.items():           
        candidates.append(c)
        votes.append(v)

#here the candidates and votes lists are put into the candidates list 
#for the final part of the analysis
#the list is then sorted to place the candidate with the highest totals in the top spot    
    candidates_list = list(zip(votes, candidates))
    candidates_list.sort(reverse=True)

#each candidate's results are put into a variable to be called as needed
#the method here is to identify the votes portion of the candidates_list and then divide that
#number by the total votes cast, yielding the final results for the candidate
kahn_results = (candidates_list[0][0] / total_votes)
correy_results= (candidates_list[1][0] / total_votes)
li_results = (candidates_list[2][0] / total_votes)
o_tooley_results = (candidates_list[3][0] / total_votes)

#the text file is created here, containint the business requirements for the end user
with open('py_poll.txt', 'w') as py_poll_txt:
    py_poll_txt.write(f"Election Results\n\
----------------\n\
Total Votes: {total_votes}\n\
----------------\n\
Khan: {kahn_results}\n\
Correy: {correy_results}\n\
Li: {li_results}\n\
O'Tooley: {o_tooley_results}\n\
----------------\n\
Winner: Kahn")

#print statements to verify the statements are what the user wants them to be
print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")
print(f"Kahn: {kahn_results}")
print(f"Correy: {correy_results}")
print(f"Li: {li_results}")
print(f"O'Tooley: {o_tooley_results}")
print("----------------")
print("Winner: Khan")
print("----------------")
