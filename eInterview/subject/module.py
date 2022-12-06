from utils.sqlConnection import mysqlConnect

# def createTable():
try:
    conn = mysqlConnect()
    sql = 'CREATE TABLE subject ( id int NOT NULL IDENTITY(1,1),subject varchar(50) NOT NULL,PRIMARY KEY (id), UNIQUE (subject));'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("questions table created")
except Exception as e:
    print(e)