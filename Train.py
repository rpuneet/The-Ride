''' This is used to get information for a particular train. '''

import bs4

import requests

import pandas as pd

from os import getcwd

class Train:
    def __init__(self , train_number = ""):
        self.train_number = train_number
        self.train_name = ""
        self.start_date = "today"
        self.train_details = []
    
    def assign_train_number(self , train_number):
        self.train_number = train_number
        
    def get_train_details(self):
        if self.train_details == []:
            print("No data to show.")
            return 0
        
        return self.train_details
    
    def retrieve_train_details(self):
        if self.train_number == "":
            print("Train number is not assigned.")
            return 0
        print("Retrieving train details from runningstatus.in ...." , end = " ")
        train_details_runningstatus_webpage = requests.get("https://runningstatus.in/status/"+self.train_number+"-"+self.start_date)
        train_details_bs4 = bs4.BeautifulSoup(train_details_runningstatus_webpage.text , 'lxml')
        
        
        table = train_details_bs4.find("table" , {"class" : "table table-striped table-bordered"})
        
        table_body = table.find('tbody')
    
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            self.train_details.append([ele for ele in cols if ele])
            
        print("Done.")
        
    def store_data_to_csv(self):
        print("Storing data in csv file ... " , end = " ")
        data_details = ["Station" , "Platform" , "Sch. Arrival" , "Sch. Departure" , "Actual Arrival / Departure" , "Avg. Speed" , "Train Status"]
        
        for index in range(len(self.train_details)):
            while len(self.train_details[index]) != 7:
                self.train_details[index].append("-")
        
        data_frame = pd.DataFrame(self.train_details , columns = data_details)
        data_frame.to_csv(getcwd() + "\\Train-Details-CSV\\" + self.train_number + ".csv" , index = False , na_rep = '-')
        print("Done.")
            