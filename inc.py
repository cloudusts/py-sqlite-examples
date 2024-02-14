#引入sqlite3以及鏈接數據庫
import sqlite3
import os
if not os.path.exists("./test.db"):
    open("./test.db", "w").close() 


conn = sqlite3.connect('./test.db')
cursor = conn.cursor()


