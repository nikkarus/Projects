# Nameplate Automation
#  Author(s): Jasmine English, Nick Jordan
# Last Edit: 7/17/18
#
#   This project automates the process of Nameplate Report production for MRM // McCann.
#   This program has the following dependencies:
#       - Virtual Environment: TBA
#       - Screen Resolution: 1366 x 768
#       - Compatible Software: Tableau 10.1 (full screen)
#       - CSV File: list_nameplates.csv

# ------------------------ IMPORTS ---------------------------
import os
import datetime
import time
import pyautogui
import pandas
# ------------------------ FUNCTIONS ---------------------------


# mouse click
def click():
    pyautogui.click()


# move to specified x, y coordinate
def move(var1, var2, var3=0):
    pyautogui.moveTo(var1, var2, var3)


# pause for x amount of time (units: seconds)
def sleep(var1):
    time.sleep(var1)


# presses specified key(s) on keyboard
def key(var1, var2='', var3='', var4=''):
    pyautogui.hotkey(var1, var2, var3, var4)


# moves cursor to Tableau icon
def moveToTableau():
    sleep(2)
    move(290, 750)
    sleep(2)
    click()
    sleep(20)


# moves cursor to Market Filter
def moveToMarket():
    sleep(2)
    move(1225, 137)
    sleep(2)
    click()
    sleep(2)


def moveToNameplate():
    sleep(2)
    move(1225, 290)
    sleep(2)
    click()
    sleep(2)


def changeMarket(mrkts):
    sleep(2)
    pyautogui.typewrite(mrkts)
    sleep(2)
    key('down')
    sleep(2)
    key('enter')
    sleep(30)

def changeNameplate(nmplts):
    sleep(2)
    pyautogui.typewrite(nmplts)
    sleep(2)
    key('down')
    sleep(2)
    key('enter')
    sleep(30)


# creates string for file name
def createFileName(reportingDate, market, division, nameplate):
    sleep(2)
    file = str(reportingDate) + "_" + str(market) + "_Nameplate_Report_" + str(division) + "_" + str(nameplate)
    pyautogui.typewrite(file)
    sleep(2)


# save file as PDF when changing directories
def saveFileDir(reportDirectory, dateLabel, market, division, nameplates):
    sleep(2)
    key('alt', 'f', 'd')
    sleep(2)
    key('enter')
    changeReportingDirectory(reportDirectory)
    createFileName(dateLabel, market, division, nameplates)
    sleep(2)
    key('enter')
    sleep(10)


# save file as PDF without changing directories
def saveFile(dateLabel, market, division, nameplates):
    sleep(2)
    key('alt', 'f', 'd')
    sleep(2)
    key('enter')
    createFileName(dateLabel, market, division, nameplates)
    sleep(2)
    key('enter')
    sleep(10)


# creates string of reporting directory
def changeReportingDirectory(reportDirectory):
    sleep(2)
    if not os.path.exists(reportDirectory):
        os.makedirs(reportDirectory)
    sleep(2)
    key('f4')
    sleep(2)
    key('ctrl', 'a')
    sleep(2)
    pyautogui.typewrite(str(reportDirectory))
    sleep(2)
    key('enter')
    sleep(2)
    # cycles through to select file name text field
    for x in range(0, 6):
        key('tab')
        sleep(1)
    sleep(3)


def createReportDirectory(dateLabel):
    vrs = 1
    reportDirectory = "C:/Site/Reports/" + np_csv.iloc[c]['MARKET'] + "/Nameplate_Report/" + str(dateLabel) + "/V" + str(vrs)
    temp = False
    while temp == False:
        if os.path.exists(reportDirectory):
            vrs = vrs + 1
            reportDirectory = "C:/Site/Reports/" + np_csv.iloc[c]['MARKET'] + "/Nameplate_Report/" + str(dateLabel) + "/V" + str(vrs)
        else:
            temp = True
            return vrs


# ------------------------ VARIABLES ---------------------------
# directory path to csv containing make/model options for pdf filters
path = "C:\_Nameplate Automation Project\list_nameplates.csv"
# "Z:\Site\Reports\list_nameplates.csv"

# reads csv file containing nameplate, division, and market information
np_csv = pandas.read_csv(path)

# today's date
today = datetime.date.today()

# first day of current month
firstOfCurrent = today.replace(day=1)

# digits of  reporting month
reportingMonth = firstOfCurrent.month - 1 if firstOfCurrent.month > 1 else 12
reportingMonth = "0" + str(reportingMonth) if reportingMonth < 10 else str(reportingMonth)

# year it was during reporting month
reportingYear = firstOfCurrent.year if firstOfCurrent.month > 1 else firstOfCurrent.year-1

# month and year string for file naming
dateLabel = str(reportingYear) + '-' + str(reportingMonth)

# ------------------------- PROCESS ----------------------------

os.startfile("C:/_Nameplate Automation Project/Global_Nameplate_Report_automation_tester.twb")
    #"Z:\Reporting_Operations\Production\Tableau_Workbooks\Global\Global_Nameplate_Report"
sleep(30)
count = list(np_csv['MARKET'])
count = len(count)
c = 0
vrs = createReportDirectory(dateLabel)
while c < count:
    prev_mk = np_csv.iloc[c - 1]['MARKET_LONG']
    curr_mk = np_csv.iloc[c]['MARKET_LONG']
    if c == 0:
        moveToMarket()
        changeMarket(np_csv.iloc[c]['MARKET_LONG'])
        moveToNameplate()
        changeNameplate(np_csv.iloc[c]['NAMEPLATE'])
        reportDirectory = "C:/Site/Reports/" + np_csv.iloc[c]['MARKET'] + "/Nameplate_Report/" + str(
            dateLabel) + "/V" + str(vrs)
        saveFileDir(reportDirectory, dateLabel, np_csv.iloc[c]['MARKET'], np_csv.iloc[c]['DIVISION'], np_csv.iloc[c]['NAMEPLATE'])
        c = c + 1
    elif prev_mk == curr_mk:
        moveToNameplate()
        changeNameplate(np_csv.iloc[c]['NAMEPLATE'])
        saveFile(dateLabel, np_csv.iloc[c]['MARKET'], np_csv.iloc[c]['DIVISION'], np_csv.iloc[c]['NAMEPLATE'])
        c = c + 1
    else:
        moveToMarket()
        changeMarket(np_csv.iloc[c]['MARKET_LONG'])
        moveToNameplate()
        changeNameplate(np_csv.iloc[c]['NAMEPLATE'])
        reportDirectory = "C:/Site/Reports/" + np_csv.iloc[c]['MARKET'] + "/Nameplate_Report/" + str(
            dateLabel) + "/V" + str(vrs)
        saveFileDir(reportDirectory, dateLabel, np_csv.iloc[c]['MARKET'], np_csv.iloc[c]['DIVISION'], np_csv.iloc[c]['NAMEPLATE'])
        c = c + 1
