''' This is used to get information for a particular train. '''

import bs4

import requests

import pandas as pd

from os import getcwd

import json

class Train:
    
    def __init__(self , train_number = "" , start = "today"):
        self.train_details = {"Train Name" : "-" , "Train Number" : "-" , "Source": "-" , "Destination":"-" , "Start Day" : "-"}
        self.train_details["Train Number"] = train_number
        self.train_details["Start Day"] = start
        self.stations = []
        
        
    def retrieve_details(self):
        if self.train_details["Train Number"] == "":
            print("Train number is not assigned.")
            return 0
        print("Retrieving details from runningstatus.in ...." , end = " ")
        
        train_details_runningstatus_webpage = requests.get("https://runningstatus.in/status/{}-{}".format(self.train_details["Train Number"] , self.train_details["Start Day"]))
        train_details_bs4 = bs4.BeautifulSoup(train_details_runningstatus_webpage.text , 'lxml')

        self.train_details["Train Name"] = train_details_bs4.title.text.split('/')[0]
        
        
        
        station_fields = ["Station Name" , "Platform" , "Scheduled Arrival" , 
                         "Scheduled Departure" , "Actual Arrival / Departure" ,
                         "Average Speed" , "Train Status"]
        
        table = train_details_bs4.find("table" , {"class" : "table table-striped table-bordered"})
        
        table_body = table.find('tbody')
        station_details = []
        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            station_details.append([ele for ele in cols if ele])
        
        for station in station_details:
            i = 0
            current_station = {}
            for data in station:
                
                current_station[station_fields[i]] = data
                i+=1
            self.stations.append(current_station)
        
        self.train_details["Source"] = self.stations[0]["Station Name"]
        self.train_details["Destination"] = self.stations[-1]["Station Name"]
        
        print("Done.")
        
    def store_to_json(self):
        
        with open(".\\Train-Details-Json\\{}.json".format(self.train_details["Train Number"]) , "w") as output_file:
            json.dump(self.__dict__ , output_file)
            

            