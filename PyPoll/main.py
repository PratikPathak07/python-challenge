import os
import csv

with open('election_data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')

    next(csv_reader, None)
    candidates = []
    votes = 0
    vote_counts = []

    for row in csv_reader:
        votes = votes + 1
        candidate = row[2]

        if candidate in candidates:
            candidate_index = candidates.index(candidate)
            vote_counts[candidate_index] = vote_counts[candidate_index] + 1

        else:
            candidates.append(candidate)
            vote_counts.append(1)

percentages = []
max_votes = vote_counts[0]
max_index = 0

for count in range(len(candidates)):
    vote_percentage = vote_counts[count]/votes*100
    percentages.append(vote_percentage)
    if vote_counts[count] > max_votes:
        max_votes = vote_counts[count]
        print(max_votes)
        max_index = count
winner = candidates[max_index]

file1 = open("Summary.txt","w")
print("Election Results")
print(f"Total Votes: {votes}")
summary = "Election Results\n"
summary = f"{summary}Total Votes: {votes}\n"
for count in range(len(candidates)):
    print(f"{candidates[count]}: {round(percentages[count],2)}%\nVote Count: {vote_counts[count]}")
    summary = f"{summary}{candidates[count]}: {round(percentages[count],2)}%\nVote Count: {vote_counts[count]}\n"
print(f"Winner: {winner}")
summary =f"{summary}Winner: {winner}"
file1.write(summary)
file1.close()