from utils.sqlConnection import mysqlConnect

# def createTable():
try:
    conn = mysqlConnect()
    sql = 'CREATE TABLE questions ( id int NOT NULL IDENTITY(1,1),question varchar(500) NOT NULL,subject_id int,link varchar(500),teacher_id int,PRIMARY KEY (id));'
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    conn.close()
    print("questions table created")
except Exception as e:
    print(e)