import pymysql

def createDb():
    try:
        # conn = pymysql.connect(
        #     host='localhost',
        #     user='root', 
        #     password = ""
        #     )
        # conn.cursor().execute('CREATE DATABASE technors')
        print("Called db")
    except Exception as e:
        print(e)
    