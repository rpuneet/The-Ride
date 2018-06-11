# The Ride

A program which retrieves information of a train (Indian Railways) from the internet and stores the data in a .json file.

# Packages Used
-Beautiful Soup
-Requests
-Pandas
-Json

# How to use?
There are two ways to use it.
1. From Command Line - Run the program in the command line in the following way
               \> py Train_Schedule.py <train_number> <start day>
train_number - This is a five digit train number.
    If train number is not provided it will ask for it during runtime.
Start day - It is the day when train starts from source station.(Ex - Today , Yesterday , etc.)
    If start day is not provided, start day will be considered today

2. Open the Train_Schedule.py file by double clicking and enter the train number.

# Output
1. A {train_number}.json file which will contain all the informations regarding the train.
2. A {train_number}.csv file which will contain a spreadsheet of the stations the train stops at.
