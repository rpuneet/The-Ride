''' This is used to get information for a particular train. '''

import bs4

import requests


def get_train_details(train_number , start_date = "today"):
    if len(train_number) != 5:
        print("Invalid train number")
        return 0
    
    train_details_runningstatus_webpage = requests.get("https://runningstatus.in/status/"+train_number+"-"+start_date)
    train_details_bs4 = bs4.BeautifulSoup(train_details_runningstatus_webpage.text , 'lxml')
    
    train_details = []
    
    table = train_details_bs4.find("table" , {"class" : "table table-striped table-bordered"})
    
    table_body = table.find('tbody')

    rows = table_body.find_all('tr')
    for row in rows:
        cols = row.find_all('td')
        cols = [ele.text.strip() for ele in cols]
        train_details.append([ele for ele in cols if ele])
        
        
    return train_details
