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
    print("="*10, "Start", i['stockName'], "="*10)
    
    # 找出現有多少條記錄 localCnt
    try:
        with open(f"data/{i['stockName']}.json", "r", encoding='utf-8') as file:
            localCnt = json.load(file)
            localCnt = localCnt['recordCnt']
    except Exception as e:
        print(e)
    
    try:
        print(">"*3, "Get hkxnews")
        response = requests.get(url=url, headers=headers)
        # 清洗數據
        content = response.text
        content = content.replace("\\\\u003cbr/\\\\u003e", "")
        content = content.replace("\\\\n", " ")
        content = content.replace("\\\\u0026#x2f;", "/")
        # content = content.replace("0026#x2f;", "/")
            
        # HKEXNEWS 上多少條記錄 recordCnt
        content = json.loads(content)
        recordCnt = content['recordCnt']

        # 對比有沒有新的記錄,有即更新
        if recordCnt != localCnt:
            print(">"*3, i['stockName'], f"發現 {recordCnt - localCnt} 條更新")
            with open(f"data/{i['stockName']}.json", "w", encoding='utf-8') as file:
                json.dump(content, file, indent=4, ensure_ascii=False)
            
        
        else:
            print(">"*3, i['stockName'], "沒有發現更新")

        print(">"*3, i['stockName'], "Done")
    except Exception as e:
        print(e)
        sys.exit(1)
