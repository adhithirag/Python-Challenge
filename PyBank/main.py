# import the os module 
import os
#import the module to read csv files
import csv
filepath = os.path.join("Resources","budget_data.csv")
output_path = os.path.join("analysis","financial_analysis.txt")

with open(filepath, 'r', encoding = 'UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    #read the header row first
    csv_header = next(csvfile)
    
   #loop through the rows after the header row

    #initialize the total number of months
    monthtotal = 0
   #define a new list to hold the values from the profits/losses column which is index 1
   #the date column is index 0
   
    totalamount = []
    amount = 0
   
    #define a list to hold the change of the profits and losses
    change_list = []
    previouschange = 0
    average_change = 0
    monthchange = 0
    monthchange_list = []

    for row in csvreader:
        monthtotal = monthtotal + 1

        amount = amount + int(row[1])

        change = int(row[1]) - int(previouschange)
        previouschange = int(row[1])
        change_list.append(change)
        
        
        

        
        

    #prints the total number of months to the terminal
    print(f"Total months: {monthtotal}")
    #prints the net amount of profits/losses to the terminal
    print(f"Total: $ {amount}")
    #prints the average change to the terminal
    print(f"Average Change: $  ")
    #prints gratest increase to the terminal 
    print(f"Greatest Increase in Profits:  ") 
    #prints greatest decrease to the terminal
    print(f"Greatest Decrease in Profits:  ")

    

    #write the results to a text file 
    with open(output_path, 'w', encoding = 'UTF-8') as txtfile:
        header = (
            f"Financial Analysis\n"
            f"----------------\n")

        txtfile.write(header)

        total_months = (
            f"Total Months: {monthtotal}\n")
        
        txtfile.write(total_months)

        total_amount = (
            f"Total: $ {amount}\n")

        txtfile.write(total_amount)

        average_change = (
            f"Average Change: $  \n")
        
        txtfile.write(average_change)


        greatest_increase = (
            f"Greatest Increase in Profits: \n")

        txtfile.write(greatest_increase)
    
        greatest_decrease = (
            f"Greatest Decrease in Profits: \n")

        txtfile.write(greatest_decrease)
   
        



        


