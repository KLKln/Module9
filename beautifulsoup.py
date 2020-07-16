import requests
import bs4 as bs


soup = bs.BeautifulSoup(open("requestResult.txt"), 'html.parser')
f = open("requestResultPretty.txt","w+")
f.writelines(soup.prettify())
f.close()
