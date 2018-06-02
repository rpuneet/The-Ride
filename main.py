''' 
This is the driver program it takes the train number to create a json file for the train details.
Train number can be provided as a command line argument or as input in the program
'''


import sys

import GetInfo


if len(sys.argv) > 1:
    train_number = sys.argv[1].strip()
else:
    train_number = input("Enter train number : ").strip()
    
start_date = "today"

train_details = GetInfo.get_train_details(train_number , start_date)

for rows in train_details:
    for cols in rows:
        print(cols , end = "    ")
    print()
    