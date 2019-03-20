import os
import csv

csvpath = os.path.join("Resources", "election_data.csv")
outputpath = os.path.join("Output", "pypoll_results.txt")

total_votes = 0
candidates_dic = {}

with open(csvpath, newline="") as csvfile:
    polldata = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvfile)
    for row in polldata:
        total_votes = total_votes + 1
        if row[2] not in candidates_dic.keys():
            candidates_dic[row[2]] = 0
        candidates_dic[row[2]] = candidates_dic[row[2]] + 1

with open(outputpath, "w") as textfile:


    print("Election Results")
    print("Election Results", file=textfile)
    print("------------------------------------")
    print("------------------------------------", file=textfile)
    print(f'Total Votes: {total_votes}')
    print(f'Total Votes: {total_votes}', file=textfile)
    print("------------------------------------")
    print("------------------------------------", file=textfile)

    for key, value in candidates_dic.items():
            rate = value/total_votes
            print(f'{key}: {rate:.3%} ({value})')
            print(f'{key}: {rate:.3%} ({value})', file=textfile)

    print("------------------------------------")
    print("------------------------------------", file=textfile)
        

    highvotevalue = 0
    for runner in candidates_dic.keys():
        if candidates_dic[runner] > highvotevalue:
            winner = runner
            highvotevalue = candidates_dic[runner]
    
    print(f'Winner: {winner}')
    print(f'Winner: {winner}', file=textfile) 
    print("------------------------------------")
    print("------------------------------------", file=textfile)
