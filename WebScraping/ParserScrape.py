# findalllinks.py - find all the links on the page

from selenium import webdriver

from selenium.common.exceptions import WebDriverException

from selenium.webdriver.firefox.options import Options

from time import sleep

import requests

import bs4


def findalllinks(url):
	# download the page

	print('parsing...')  # displaying text while parsing the page

	res = requests.get(url)  # takes the string of the url to download

	res.raise_for_status()  # will raise exception if error downloading

	# retrieve all the links

	abhiSoup = bs4.BeautifulSoup(res.text, 'html.parser')

	linkel = abhiSoup.select('body a')  # could be altered as required

	# return a set of links

	numOpen = len(linkel)

	# print (numOpen) #optional for console validation

	linkel2 = []

	for i in range(numOpen):
		linkel2 = linkel2 + [(linkel[i].get('href'))]

	return linkel2


def pagehits(url):
	global HTML_string

	# visit the page in a headless version of firefox

	options = Options()

	options.add_argument("--headless")

	# starting selenium controlled web browser

	# latest geckodriver is needed to run firefox with selenium

	browser = webdriver.Firefox(firefox_options=options, executable_path="C:\\Users\\folderForDriver\\geckodriver.exe")

	browser.get(url)

	# give page time to load

	sleep(1)

	# log events and pagename

	# put the block in try/except

	try:

		pageName = browser.execute_script("return (s.pageName);")

		events = browser.execute_script("return (s.events);")

		print(pageName)  # optional for console validation

		print(events)  # optional for console validation

		HTML_string += '''<tr>

        <td>{}</td>

        <td>{}</td>

        <td>{}</td>'''.format(url, pageName, events)

		HTML_string += "</tr>"





	except WebDriverException:

		print("Exception on {}".format(url))

	browser.quit()






target_url = input("Enter URL for Parsing:",)

url_list = findalllinks(target_url)

# Iterate the links and collect data

for i in range(len(url_list)):

#for i in range(10,15): #optional for initial validation

    tag_link = str(url_list[i])

    if tag_link.startswith('/'):

        pagehits(target_url+tag_link)

    elif tag_link.startswith('http' or 'www'):

        pagehits(tag_link)

    else:

        continue