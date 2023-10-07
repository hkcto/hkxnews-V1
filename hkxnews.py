import requests
import sqlite3
import sys
from config import SEHK
import json
from sql import SQL
from gmail import Gmail
from gmail import createMessage


# 全區變量
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.41"
}
# Gmail smtp
gmail = Gmail(username="hkcto.com@gmail.com", secret="qtjdbtvgysljmpup")


for i in SEHK:
    
    # 數據庫實例化
    database = f"{i['stockName']}"
    sql = SQL(database)
    print("////////////////////////////////////////")
    url = f"https://www1.hkexnews.hk/search/titleSearchServlet.do?sortDir=0&sortByOptions=DateTime&category=0&market=SEHK&stockId={i['stockId']}&documentType=-1&fromDate=19990401&toDate=20230926&title=&searchType=0&t1code=-2&t2Gcode=-2&t2code=-2&rowRange=200&lang={i['lang']}"
    print("="*10, "Start", i['stockName'], "="*10)
    
    # 找出現有多少條記錄 localCnt
    try:
        with open(f"data/{i['stockName']}.json", "r", encoding='utf-8') as file:
            localCnt = json.load(file)
            localCnt = localCnt['recordCnt']
        
        sql.create()
    
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

        # 對比有沒有新的記錄,有,即更新
        if recordCnt != localCnt:
            log = f"{i['stockName']}, 發現 {recordCnt - localCnt} 條更新"
            message = createMessage(log)
            print(">"*3, log)
            with open(f"data/{i['stockName']}.json", "w", encoding='utf-8') as file:
                json.dump(content, file, indent=4, ensure_ascii=False)
       
       
            ### here for update code ####    
        
        else:
            print(">"*3, i['stockName'], "沒有發現更新")

            data = json.loads(content['result']) # 將 result 的內容轉為 list 類型
            for item in data:
                try:
                    sql.dict_insert(data=item)
                except sqlite3.IntegrityError:
                    print("忽略重复数据:", item)

        print(">"*3, i['stockName'], "Done")
        sql.close()
    except Exception as e:
        print(e)
        sys.exit(1)
