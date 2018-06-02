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


train = Train.Train(train_number)
train.retrieve_train_details()
#train_details = train.get_train_details()
train.store_data_to_csv()

#print(train_details)
