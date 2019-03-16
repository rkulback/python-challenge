import os
import csv

pypoll_data = os.path.join(".", "election_data.csv")

total_votes = 0             
candidates_results = {}        
candidates_list = []        

with open(pypoll_data, newline="") as election_data_file:
    election_results = csv.DictReader(election_data_file)

    for row in election_results:
        total_votes += 1                           
    
        if row['Candidate'] not in candidates_results:  
            candidates_results[row['Candidate']] = 0    
    
        if row['Candidate'] in candidates_results:      
            candidates_results[row['Candidate']] = candidates_results[row['Candidate']] + 1
  
    candidates = []     
    votes = []                           
                                       
    for c, v in candidates_results.items():           
        candidates.append(c)
        votes.append(v)
        
    candidates_list = list(zip(votes, candidates))
    candidates_list.sort(reverse=True)

kahn_results = (candidates_list[0][0] / total_votes)
correy_results= (candidates_list[1][0] / total_votes)
li_results = (candidates_list[2][0] / total_votes)
o_tooley_results = (candidates_list[3][0] / total_votes)

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

print("Election Results")
print("----------------")
print(f"Total Votes: {total_votes}")
print("----------------")
print(f"Kahn: {kahn_results}")
print(f"Correy: {correy_results}")
print(f"Li: {li_results}")
print(f"O'Tooley: {o_tooley_results}")
print("Winner: Khan")
