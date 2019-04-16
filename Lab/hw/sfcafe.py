from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel
from collections import OrderedDict

url = "http://s.cafef.vn/bao-cao-tai-chinh/VNM/IncSta/2017/3/0/0/ket-qua-hoat-dong-kinh-doanh-cong-ty-co-phan-sua-viet-nam.chn"
conn = urlopen(url)
raw_data = conn.read()
html_content = raw_data.decode('utf8')


soup = BeautifulSoup(html_content,"html.parser")
table = soup.find('table', id="tableContent")
td_number = table.find_all('td', attrs={'class':'b_r_c', 'align':'right', 'style':'width:15%;padding:4px;color:#014377;'})
td_healines1 = table.find_all('td', attrs={"style":"width:32%;color:#014377;font-weight:bold;","class":"b_r_c"})
td_healines2 = table.find_all('td', attrs={"style":"width:32%;color:#014377;","class":"b_r_c"})
td_healines = td_healines1 + td_healines2
Result = []
i = 0
for td1 in td_healines:
    headlines = td1.string.strip()
    item = OrderedDict({'headlines':headlines})
    for td2 in td_number:
        number = td2.string
        if number == None:
            number = ''
        else:
            for i in range(len(td_number)):
                item['Quy III - 2017'] = number[i]
                item['Quy II - 2017'] = number[i+1]
                item['Quy I -2017'] = number[i+2]
                item['Quy IV - 2016'] = number[i+3]
                i += 4
    Result.append(item)

print(Result)

# pyexcel.save_as(records=Result, dest_file_name="cafef.xlsx")













