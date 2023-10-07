import sqlite3

class SQL():
    def __init__(self, database: str) -> None:
        self.database = database
        self.conn = sqlite3.connect(f'{self.database}.db')
        self.cursor = self.conn.cursor()
    
    def create(self):
        
        self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS '{self.database}' (
                FILE_INFO TEXT,
                NEWS_ID TEXT,
                SHORT_TEXT TEXT,
                TOTAL_COUNT TEXT,
                DOD_WEB_PATH TEXT,
                STOCK_NAME TEXT,
                TITLE TEXT,
                FILE_TYPE TEXT,
                DATE_TIME TEXT,
                LONG_TEXT TEXT,
                STOCK_CODE TEXT,
                FILE_LINK TEXT,
                ACTIVE INT
            )
        ''')
        self.conn.commit()
        print(f"Creat {self.database}")

    def dict_insert(self, data: dict):
        keys = ', '.join(data.keys())
        placeholders = ', '.join([':' + key for key in data.keys()])
        query = f"""INSERT OR IGNORE INTO '{self.database}' ({keys}) VALUES ({placeholders})"""
        self.cursor.execute(query, data)
        self.conn.commit()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__=="__main__":
    sql = SQL("test")
    sql.create()
    query = {'FILE_INFO': '436KB', 'NEWS_ID': '10901938', 'SHORT_TEXT': 'Announcements and Notices - [Major Transaction]', 'TOTAL_COUNT': '173', 'DOD_WEB_PATH': '', 'STOCK_NAME': 'PER ENERGY', 'TITLE': "MAJOR TRANSACTION WRITTEN SHAREHOLDER'S APPROVAL", 'FILE_TYPE': 'PDF', 'DATE_TIME': '19/09/2023 17:53', 'LONG_TEXT': 'Announcements and Notices - [Major Transaction]', 'STOCK_CODE': '02798', 'FILE_LINK': '/listedco/listconews/sehk/2023/0919/2023091900699.pdf'}
    sql.dict_insert(query)
    sql.close()