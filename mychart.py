import csv
import matplotlib.pyplot as plt
import os
# get date and time
from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%m_%d_%Y")

def getDirectory():
    directory = "Output_" + dt_string
    return directory

def generateChart(displayChart):

    # get the directory
    directory = getDirectory()

    print("Generating chart")

    # Initialize the data
    data = {}
    counts = {}

    # Read the CSV file and store the data in a dictionary
    with open(directory + "\chartData.csv", "r") as f:
        reader = csv.reader(f)
        for row in reader:
            name = row[0]
            value = int(row[1])
            if name not in data:
                data[name] = []
                counts[name] = 0
            data[name].append(value)
            counts[name] += 1

    # Plot the data
    fig, ax = plt.subplots()
    for name, values in data.items():
        # Format the name
        ax.plot(values, label=name)

    # Add a legend and move it to the right side of the plot
    ax.legend(loc="center left", bbox_to_anchor=(1, 0.5))

    # Adjust the plot dimensions to make room for the legend
    plt.subplots_adjust(right=0.7)


    plt.grid(True)

    # pageRequests = int(counts[name])
    # Add a legend and show the plot
    plt.xlabel("Page Requests")
    plt.ylabel("Percentage of Ads Found")
    # set the x axis to 0 to max of page requests
    # plt.xlim(0, 100)
    plt.title("Page Requests")
    # plt.show()

    # save the chart
    plt.savefig(directory + "\chart.png")

    if displayChart == "True":
        os.startfile(directory+"\chart.png")




