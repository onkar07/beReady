from utils.sqlConnection import mysqlConnect

def registerUser():
    try:
        conn = mysqlConnect()
        cur = conn.cursor()
        try:
            sql1 = "CREATE TABLE [user] (id INT NOT NULL IDENTITY(1,1),name VARCHAR(25) NOT NULL, email VARCHAR(25) NOT NULL, password VARCHAR(25), role VARCHAR(25) ,PRIMARY KEY (id), UNIQUE (email))"
            cur.execute(sql1)
        except Exception as e:
            print("creatre",e)
        try:
            sql = "INSERT INTO [user] (name, email, password, role) VALUES ('sudo', 'sudo@gamil.com', 'sudo@123', 'sudo');"
            cur.execute(sql)
        except Exception as e:
            print("Insert",e)
        conn.close()
        print("Sudo User Register")
    except Exception as e:
        print("Error in register user",e)
    
def registerUserByApi(request):
    try:
        data=request.get_json()

        name = data.get('name')
        email = data.get('email')
        password=data.get('password')
        role='student'
        conn = mysqlConnect()
        cur = conn.cursor()
        try:
            sql = "INSERT INTO [user] (name, email, password, role) VALUES (%s,%s,%s,%s);"
            val = (name,email,password,role)
            cur.execute(sql,val)
            conn.commit()
            conn.close()
            print("User Register")
            conn.close()
            return {"msg":"success"}
        except Exception as e:
            print("Insert",e)
            return {"msg":"failed"}
    except Exception as e:
        print("Error in register user",e)
        return {"msg":"error"}  
    