import webbrowser, requests, bs4
########################################

#webbrowser.open('https://gmcertified.com')

res = requests.get('http://gmcertified.com')
res.raise_for_status()
gmCertifiedSoup = bs4.BeautifulSoup(res.text, "html.parser")
type(gmCertifiedSoup)

pElems = gmCertifiedSoup.select('author')
print(type(pElems))
print(str(pElems[0]))