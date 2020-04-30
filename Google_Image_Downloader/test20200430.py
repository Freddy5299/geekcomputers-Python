from urllib.request import urlopen, Request
import requests
from bs4 import BeautifulSoup

usr_agent = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,zh-TW;q=0.8,en-US;q=0.7,en;q=0.6',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
               '(KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36',
    'Connection': 'keep-alive',
}
g = 'https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q=ipad'
request = requests.get(g, headers=usr_agent)

sew = BeautifulSoup(request.text, 'html.parser')
results = sew.findAll('img', {'class': 'rg_i Q4LuWd tx8vtf'})
print(results)