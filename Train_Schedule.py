''' 
This is the driver program it takes the train number to create a json file for the train details.
Train number can be provided as a command line argument or as input in the program
'''


import sys

import Train

if len(sys.argv) > 1:
    train_number = sys.argv[1].strip()
else:
    train_number = input("Enter train number : ").strip()

start_day = "today"

if len(sys.argv) > 2:
    start_day = sys.argv[2].strip()

train = Train.Train(train_number = train_number , start = start_day)
train.retrieve_details()
train.store_to_json()
