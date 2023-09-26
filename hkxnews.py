import requests
import sys
from config import SEHK

# 全區變量
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"
}

for i in SEHK:
    
    url = f"https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime&category=0&market=SEHK&stockId={i['stockId']}&documentType=-1&fromDate=19990401&toDate=20230926&title=&searchType=0&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=200&lang={i['lang']}"
    try:
        print("="*10, "Start", i['stockName'], "="*10)
        response = requests.get(url=url, headers=headers)
        print(response.text)
    except Exception as e:
        print(e)
        sys.exit(1)