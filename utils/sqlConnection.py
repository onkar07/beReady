import pymssql
def mysqlConnect():
    try:
        conn = pymssql.connect("103.21.58.192", "eleuser", "Rwc9~d74", "demo16")
        # cursor = conn.cursor()
        # cursor.execute('select name FROM sys.databases')
        # for rows in cursor:
        #     print(rows)
        return conn
    except Exception as e:
        print(e)
    
# mysqlConnect()

# import pyodbc 
# # Some other example server values are
# # server = 'localhost\sqlexpress' # for a named instance
# # server = 'myserver,port' # to specify an alternate port
# server = '103.21.58.192' 
# database = 'demo16' 
# username = 'eleuser' 
# password = 'Rwc9~d74' 
# # ENCRYPT defaults to yes starting in ODBC Driver 18. It's good to always specify ENCRYPT=yes on the client side to avoid MITM attacks.
# cnxn = pyodbc.connect('DRIVER={{SQL Server}};SERVER='+server+';DATABASE='+database+';ENCRYPT=yes;UID='+username+';PWD='+ password)
# cursor = cnxn.cursor()

# conn = pymssql.connect("103.21.58.192", "eleuser", "Rwc9~d74", "demo16")
# cursor = conn.cursor()
# cursor.execute('select name FROM sys.databases')
# for rows in cursor:
#     print(rows)
# print(cursor)
# return conn