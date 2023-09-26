import requests
import sys
from config import SEHK
import json

# 全區變量
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"
}

for i in SEHK:
    
    url = f"https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime&category=0&market=SEHK&stockId={i['stockId']}&documentType=-1&fromDate=19990401&toDate=20230926&title=&searchType=0&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=200&lang={i['lang']}"
    try:
        print("="*10, "Start", i['stockName'], "="*10)
        print(">"*3, "Get hkxnews")
        response = requests.get(url=url, headers=headers)
        content = response.text.replace("\\\\u003cbr/\\\\u003e\\", "")
        
        print(">"*3, f"保存: {i['stockName']}.json")
        with open(f"{i['stockName']}.json", "w", encoding="utf-8") as f:
            json.dump(content, f, indent=4, ensure_ascii=False)
        
        print(">"*3, i['stockName'], "Done")
    except Exception as e:
        print(e)
        sys.exit(1)