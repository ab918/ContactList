import csv

def readFile():

    with open('50-contacts.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            print(row)
    csvFile.close

def filterFName(firstName):

def filterLName(lastName):

def filterCountry(country):

def filterState(state):

def filterZIP(zip):

def filterCompany(comp):

def addRegistry():

def removeRegistry():

def deleteTable():

def createTable():

readFile()
