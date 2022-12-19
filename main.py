import threading

# get Variable from config.ini
import configparser
import json
from myadcheck import *
from mychart import *

config = configparser.ConfigParser()
config.read('config.ini')
sellerID = config['General']['SellerName']
pageRequests = config['General']['FetchCount']
htmlBool = config['General']['DisplayHTML']
displayChart = config['General']['DisplayChart']
multiThread = config['General']['MultiThread'] 

if multiThread == "True":
    with open('pages.json') as json_file:
        data = json.load(json_file)
        threads = []
        for p in data:
            pageName = p
            pageURL = data[p]
            t = threading.Thread(target=CheckAds, args=(sellerID, pageRequests, htmlBool, pageName, pageURL, multiThread))
            threads.append(t)
            t.start()

        # Wait for all threads to complete
        for t in threads:
            t.join()
else:
    with open('pages.json') as json_file:
        data = json.load(json_file)
        for p in data:
            pageName = p
            pageURL = data[p]
            CheckAds(sellerID, pageRequests, htmlBool, pageName, pageURL, multiThread)

generateChart(displayChart)