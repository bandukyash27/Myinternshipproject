from bs4 import BeautifulSoup
import  urllib.request
from IPython.display import HTML
import re
r=urllib.request.urlopen("https://www.crummy.com/software/BeautifulSoup/").read()
soup=BeautifulSoup(r,"lxml")
                #showing type of the soup
print(type(soup))
                #showing href links
for link in soup.find_all("a"):
    print(link.get("href"))
                #showing text of the website
print(soup.get_text())
print(soup.prettify()[0:1000])
for link in soup.find_all("a",attrs={"href":re.compile("^http")}):
    print(link)
type(link)
                #parsing a data from website
file=open("parsed_data.txt","w")
for link in soup.find_all("a",attrs={"href":re.compile("^http")}):
    soup_link=str(link)
    print(soup_link)
    file.write(soup_link)
file.flush()
file.close()

                                     
