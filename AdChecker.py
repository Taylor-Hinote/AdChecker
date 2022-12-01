import requests
import sys
import os
from bs4 import BeautifulSoup

# if command line arguments are not provided then exit
if len(sys.argv) < 2:
    for x in range(5):
        print()
    print('Usage: python AdChecker.py <url> <seller> <trials>') 
    print("Please provide the URL as command line argument")
    print("Example: python AdChecker.py https://www.google.com/search?q=marble+fountain ''Fine's Gallery'' 10")
    for x in range(5):
        print()
    sys.exit()
# Get the URL from the command line
url = sys.argv[1]
# Get Seller ID from the command line
sellerID = sys.argv[2]

# get pageRequest from command line
pageRequests = sys.argv[3]

# Get int from command line and convert to int
pageRequests = int(pageRequests)

headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36" }
percentage = 0

params = url.replace("https://www.google.com/search?q=", "")
params = params.replace("+", "_")

# get date and time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%m_%d_%Y")

directory = "Output_" + dt_string
subDirectory = params.title()
directoryFinal = directory + "/" + subDirectory
os.makedirs(directoryFinal+'\ScreenShots', exist_ok=True)
fileName = directoryFinal+"\Page Request.html"

f = open(fileName, "w", encoding="utf-8")
f.write("<html><head><title>Page Request</title></head><body>")

f.write('<div style="text-align: center;"><h1>Page Requests</h1><p>Results for <strong><a href="'+url+'" target="_blank">'+ url +'</a></strong> ran <strong>' + str(pageRequests) +'</strong> times</p></div>')
f.write('<div style="text-align: center;"<strong><a href="#bottom">Bottom of Page </a></strong></div>')

for x in range(5):
    print()
print("Checking for ads from " + sellerID + " on " + url)
for x in range(pageRequests):
    print("Fetching page: ", x+1)

    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    s = open(directoryFinal + "\ScreenShots\ScreenShot"+ str(x+1) +".html", "w", encoding="utf-8")
    s.write(soup.prettify())
    s.close()

    cards = soup.find_all("div", class_="mnr-c")
    sellers = soup.find_all("span", class_="zPEcBd VZqTOd")
    sellers2 = soup.find_all("span", class_="rhsg3")
    caroseul = soup.find("div", class_="bC8sde BNizGe")
    totalCards = 0
    totalSeller = 0
    for card in cards:
        totalCards += 1
    for seller in sellers:
        if(seller.text == sellerID):
            totalSeller += 1
    for seller in sellers2:
        if(seller.text == sellerID):
            totalSeller += 1
            
    
    f.write("<h1>Page: " + str(x+1) + "</h1>")
    print ("Total Ad's: ", totalCards)
    f.write("Total Ad's: " + str(totalCards))
    f.write("<br>")
    print (sellerID +" appears: ", totalSeller)
    f.write(sellerID +" appears: " + str(totalSeller))
    f.write("<br>")
    print ("Percentage: ", (totalSeller/totalCards)*100)
    f.write("Percentage: " + str((totalSeller/totalCards)*100))
    f.write("<h3>Page Preview</h3>")
    f.write('<iframe style="resize: both; border-radius: .25em; border:1px solid black; 	box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5)  ;-webkit-box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5)  ; -moz-box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5)  ; "src="./ScreenShots/ScreenShot'+ str(x+1) +'.html" width=1200px height=300px></iframe>')
    f.write("<br>")
    f.write("<br>")
    print()
    print()
    percentage = percentage + (totalSeller/totalCards)*100

totalPercentage = percentage / pageRequests

print(f"{sellerID} is selling on average {round(totalPercentage, 2)}% of the items on \n {url} tested {pageRequests} times.")
for x in range(2):
    print()
print("Results have been saved to "+directoryFinal+"\Page Request.html")
for x in range(2):
    print()
    
f.write('<div style="text-align: center;">')
f.write("<h1>Summary</h1>")
f.write("<a id='bottom'></a>")
f.write(f"<p><strong>{sellerID}</strong> is selling on average <strong>{round(totalPercentage, 2)}%</strong> of the items on \n <strong>{url}</strong> tested <strong>{pageRequests}</strong> times.</p>")
f.write("<br>")
f.write("</div>")


f.close()

os.startfile(fileName, 'open')