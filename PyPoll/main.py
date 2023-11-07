import os
import csv 
import numpy as np

filepath = os.path.join("Resources","election_data.csv")
output_path = os.path.join("analysis","election_results.txt")

with open(filepath, 'r', encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header row first
    csv_header = next(csvfile)

    totalvotes = 0
    candidate_list = []

    for row in csvreader:
        totalvotes = totalvotes + 1
        candidate = row[2]
        candidate_list.append(candidate)

    
    
    #this will give us an array with the count occurrences of each unique value
    candidate_array = np.unique(candidate_list, return_counts= True)
    #this converts the input which is candidate_array int to an array
    new_array = np.asarray((candidate_array)).T

    #name of the first candidate
    candidate1 = (candidate_array[0][0])
    #name of the second candidate
    candidate2 = (candidate_array[0][1])
    #name of the third candidate
    candidate3 = (candidate_array[0][2])
    # number of votes that the first candidate received
    votes1 = (candidate_array[1][0])
    # number of votes that the second candidate received
    votes2 = (candidate_array[1][1])
    # number of votes that the third candidate received
    votes3 = (candidate_array[1][2])

    #percentage of votes won by each candidate 
    percentage1 = round(((int(votes1))/ totalvotes) *100 , 3)
    
    percentage2 = round(((int(votes2))/ totalvotes) *100 , 3)
    
    percentage3 = round(((int(votes3))/ totalvotes) *100 , 3)

    #define the maximum variable that will hold the max number of votes won by a candidate
    maximum = np.max(candidate_array[1])

    #define winner variable as the candidate who received the max number of votes
    
    #write the results to a text file 
    with open(output_path, 'w', encoding = 'UTF-8') as txtfile:
        header = (
            f"Election Results\n"
            f"----------------\n")

        txtfile.write(header)

        total_votes = (
            f"Total Votes: {totalvotes}\n"
            f"-------------------------\n")

        
        txtfile.write(total_votes)

        candidate_names = (
            f"{candidate1} : {percentage1} % ({int(votes1)})\n"

            f"{candidate2} : {percentage2} % ({int(votes2)})\n"

            f"{candidate3} : {percentage3} % ({int(votes3)})\n"

            f"----------------------------------------------\n")
        
        txtfile.write(candidate_names)
        
        winner = (
            f"Winner: \n"

            f"The winner received {maximum} votes.\n"

            f"-------------------------------------\n")
        
        txtfile.write(winner)


    #print the total number votes to the terminal 
    print(f" Total Votes: {totalvotes}")
    #print name of the first candidate, the percentage of votes they won, and the number of votes they received 
    print(f"{candidate1} : {percentage1} % ({int(votes1)})") 
    #print name of the second candidate, the percentage of votes they won, and the number of votes they received 
    print(f"{candidate2} : {percentage2} % ({int(votes2)})") 
    #print name of the third candidate, the percentage of votes they won, and the number of votes they received 
    print(f"{candidate3} : {percentage3} % ({int(votes3)})") 
   
   #print the number of votes that the winner received
    print(f"The winner received {maximum} votes.")
   
    #print the name of the winner who received the max number of votes 
    print(f"Winner: ") 