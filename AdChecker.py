import requests
import sys
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

for x in range(5):
    print()
print("Checking for ads from " + sellerID + " on " + url)
for x in range(pageRequests):
    print("Fetching page: ", x+1)

    page = requests.get(url, headers=headers)


    soup = BeautifulSoup(page.content, "html.parser")

    cards = soup.find_all("div", class_="mnr-c")
    sellers = soup.find_all("span", class_="zPEcBd VZqTOd")
    totalCards = 0
    totalSeller = 0
    for card in cards:
        totalCards += 1
    for seller in sellers:
        if(seller.text == sellerID):
            totalSeller += 1
    
    print ("Total Cards: ", totalCards)
    print ("Total Seller: ", totalSeller)
    print ("Percentage: ", (totalSeller/totalCards)*100)
    print()
    print()
    percentage = percentage + (totalSeller/totalCards)*100

totalPercentage = percentage / pageRequests

print(f"{sellerID} is selling on average {totalPercentage}% of the items on \n {url} tested {pageRequests} times.")
for x in range(2):
    print()
