#imports first
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

#Lists to store data
voter_ids = []
candidates = []
candidate_names = []
votes_per_candidate = []
percentage_votes = []
winnervotes = 0

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    print(csvreader)

    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    for row in csvreader:
        voter_ids.append(row[0])
        candidates.append(row[2])

    #sets the total amount of votes to the length of the list with voter ids
    total_votes = len(voter_ids)
    

    #adds the first candidate name in the candidates list to the candidate name
    candidate_names.append(candidates[0])

    #for loop to compare if a candidate is different from next one and if that name isn't in the list of candidate names, then update
    for x in range(total_votes - 1):
        if candidates[x+1] != candidates[x] and candidates[x+1] not in candidate_names:
            candidate_names.append(candidates[x+1])

    #just checking how many different names appear in the file
    candidate_list = len(candidate_names)
    
    
    #for loop to add the total number of votes each candidate received
    for x in range (candidate_list):
        votes_per_candidate.append(candidates.count(candidate_names[x]))
        percentage_votes.append(f"{round((votes_per_candidate[x]/total_votes*100),3)}%")
        
    winner = candidate_names[votes_per_candidate.index(max(votes_per_candidate))]
    # candidate_results = list(zip(candidate_names, percentage_votes, votes_per_candidate))

    #below is coded out print statements I used to verify my code was accurate
    # print(total_votes)
    # print(candidate_list)
    # print(candidate_names)
    # print(votes_per_candidate)
    # print(percentage_votes)
    # print(winner)
    # print(candidate_results)

    print("Election Results")
    print("-------------------------")
    print("Total Votes: " + str(total_votes))
    print("-------------------------")
    print(f"{candidate_names[0]}: {percentage_votes[0]} ({votes_per_candidate[0]})")
    print(f"{candidate_names[1]}: {percentage_votes[1]} ({votes_per_candidate[1]})")
    print(f"{candidate_names[2]}: {percentage_votes[2]} ({votes_per_candidate[2]})")
    print("-------------------------")
    print(f"Winner: {winner}")
    print("-------------------------")

    output_file = os.path.join('..', 'Analysis','output.txt')

    with open(output_file, "w", newline='') as textfile:
        writer = csv.writer(textfile, delimiter=",")

        textfile.write("Election Results " + "\n")
        textfile.write("-------------------------" + "\n")
        textfile.write("Total Votes: " + str(total_votes) + "\n")
        textfile.write("-------------------------" + "\n")
        textfile.write(f"{candidate_names[0]}: {percentage_votes[0]} ({votes_per_candidate[0]})" + "\n")
        textfile.write(f"{candidate_names[1]}: {percentage_votes[1]} ({votes_per_candidate[1]})" + "\n")
        textfile.write(f"{candidate_names[2]}: {percentage_votes[2]} ({votes_per_candidate[2]})" + "\n")
        textfile.write("-------------------------" + "\n")
        textfile.write(f"Winner: {winner} " + "\n")
        textfile.write("-------------------------" + "\n")

        textfile.close()


    