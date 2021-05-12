import requests
from lxml import etree
# import matplotlib.pyplot as mlt
# import seaborn as sns


url='https://www.timeshighereducation.com/world-university-rankings/2021/world-ranking#!/page/0/length/25/sort_by/name/sort_order/asc/cols/stats'

headers={
    'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}

response = requests.get(url,headers).text
print(response)










