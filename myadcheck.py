import os
import requests
from bs4 import BeautifulSoup
import sys

def CheckAds(sellerID, pageRequests, htmlBool, pageName, pageURL, multiThread):
    # Get int from command line and convert to int
    pageRequests = int(pageRequests)

    headers = { "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36" }
    percentage = 0

    # params = pageURL.replace("https://www.google.com/search?q=", "")
    # params = params.replace("+", "_")

    params = pageName

    # get date and time
    from datetime import datetime
    now = datetime.now()
    dt_string = now.strftime("%m_%d_%Y")

    def getDirectory():
        directory = "Output_" + dt_string
        return directory


    # directory = "Output_" + dt_string
    directory = getDirectory()
    subDirectory = params.title()
    directoryFinal = directory + "/" + subDirectory
    os.makedirs(directoryFinal+'\ScreenShots', exist_ok=True)
    fileName = directoryFinal+"\Page Request.html"

    f = open(fileName, "w", encoding="utf-8")
    f.write("<html><head><title>Page Request</title></head><body>")

    f.write('<div style="text-align: center;"><h1>Page Requests</h1><br>.<h2>'+ params +'</h2> <p><strong><br><a href="'+pageURL+'" target="_blank">'+ pageURL +'</a></strong> ran <strong>' + str(pageRequests) +'</strong> times</p></div>')
    f.write('<div style="text-align: center;"<strong><a href="#bottom">Bottom of Page </a></strong></div>')

    print("Checking for ads from " + sellerID + " on " + pageURL)

    # init an array to store results for chart
    chartArray = []

    # init a csv file to store results for chart if a file does not already exist
    import csv
    if not os.path.exists(directory + '\chartData.csv'):
        with open(directory + '\chartData.csv', 'w', newline='') as file:
            writer = csv.writer(file)


    for x in range(pageRequests):
        # if error occurs then go continue to next page
        try:
            print(" "* 100, end="\r")
            print("Fetching page "+ pageName +": ", x+1 , end="\r")

            page = requests.get(pageURL, headers=headers)

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
            
            if multiThread == "False":
                print ("Total Ad's: ", totalCards)
                print (sellerID +" appears: ", totalSeller)
                print ("Percentage: ", (totalSeller/totalCards)*100)
                print()
                print()
            
            f.write("<h1>Page: " + str(x+1) + "</h1>")
            f.write("Total Ad's: " + str(totalCards))
            f.write("<br>")
            f.write(sellerID +" appears: " + str(totalSeller))
            f.write("<br>")
            f.write("Percentage: " + str((totalSeller/totalCards)*100))
            f.write("<h3>Page Preview</h3>")
            f.write('<iframe style="resize: both; border-radius: .25em; border:1px solid black; 	box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5)  ;-webkit-box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5)  ; -moz-box-shadow: 5px 5px 20px rgba(0, 0, 0, 0.5)  ; "src="./ScreenShots/ScreenShot'+ str(x+1) +'.html" width=1200px height=300px></iframe>')
            f.write("<br>")
            f.write("<br>")
            percentage = percentage + (totalSeller/totalCards)*100
            chartArray.append((totalSeller/totalCards)*100)
            with open(directory + '\chartData.csv', 'a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([params, round((totalSeller/totalCards)*100)])
        except:
            if multiThread == "False":
                print("Error occured on page: ", x+1)
                print("Continuing to next page...")
                print()
                print()
            continue


    totalPercentage = percentage / pageRequests
    f.write('<div style="text-align: center;">')
    f.write("<h1>Summary</h1>")
    f.write("<a id='bottom'></a>")
    f.write(f"<p><strong>{sellerID}</strong> is selling on average <strong>{round(totalPercentage, 2)}%</strong> of the items on \n <strong>{pageURL}</strong> tested <strong>{pageRequests}</strong> times.</p>")
    f.write("<br>")
    f.write("</div>")

    f.close()

    if multiThread == "False":
        print(f"{sellerID} is selling on average {round(totalPercentage, 2)}% of the items on \n {pageURL} tested {pageRequests} times.")
        for x in range(2):
            print()
    print("Results have been saved to "+directoryFinal+"\Page Request.html")
        

    if(htmlBool == "True"):
        os.startfile(fileName, 'open')

    return


