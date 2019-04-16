from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

# 1. Connection
url = "https://dantri.com.vn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')

with open("dantri.html","wb") as f:
    f.write(raw_data)

# 2. Find ROI (region of interest)
soup = BeautifulSoup(html_content,"html.parser")
ul = soup.find('ul','ul1 ulnew') # attribute "class" ko can type ra

# 3.Extract ROI
li_list = ul.find_all('li')
Result =[]
for li in li_list:
    h4 = li.h4
    a = h4.a
    title = a.string.strip()
    link  = url + a['href']
    phantu = OrderedDict({"Title":title,"Link":link})
    Result.append(phantu)

# pyexcel.save_as(records=Result, dest_file_name="test.xlsx")