import mysql.connector 
import json 

class Query_Mysql :
    
    def create_table():
    # create table user inside database if not exists
        table_script = "CREATE TABLE IF NOT EXISTS Information(id VARCHAR(255) , Name VARCHAR(255),Age INT(255), Sex VARCHAR(255), Class VARCHAR(255),PRIMARY KEY (id) );"
        db = mysql.connector.connect(user= 'root', password = 'Dunggttn1512.', host='localhost', database='Student')
        mycursor = db.cursor()
        mycursor.executescript(table_script)
        db.commit()
    
    def insert_data(id , Name, Age , Sex , Class):

        conn = mysql.connector.connect(
        user='root', password='Dunggttn1512.', host='localhost', database='Student')
        cursor = conn.cursor()
        sql =f"INSERT INTO Information(id, Name, Age, Sex, Class) VALUES ('{id}', '{Name}', {Age}, '{Sex}', '{Class}')"
        print(sql)

        try:
            cursor.execute(sql)
            conn.commit()

        except:
            conn.rollback()
            conn.close()
    
    "function update data in mysql"
    def update_data(id, Name , Age , Sex, Class):

        conn = mysql.connector.connect(user= 'root', password = 'Dunggttn1512.', host='localhost', database='Student')
        cursor = conn.cursor()
        sql =f"UPDATE Information SET Name =' {Name}' , Age= {Age} , Sex= '{Sex}', Class= '{Class}' WHERE id = {id}"
        print(sql)
        try: 
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            conn.close()
    

    def insert_data_file_upload(id,filename,address, id_drive) :   
        conn = mysql.connector.connect(
        user= 'root' , password = 'Dunggttn1512.', host='localhost', database='Student')
        cursor = conn.cursor()
        sql =f"INSERT INTO fileupload(id, filename, address,id_drive) VALUES ('{id}', '{filename}', {address}, {id_drive})"
        try: 
            cursor.execute(sql)
            conn.commit()
        except:
            conn.rollback()
            conn.close()

    def get_drive_id_from_fileupload(m):
        result_final = []
        db = mysql.connector.connect(
        user= 'root' , password = 'Dunggttn1512.', host='localhost', database='Student')
        mycursor = db.cursor()
        sql = "SELECT id_drive FROM fileupload WHERE id = %s" %(m)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        result_final.append(result)
        # result1=result[0]
        # result_final = json.dumps(result1)
        db.commit()
        db.close()
        return result_final


    def get_filename_from_fileupload(m):
        result_final = []
        db = mysql.connector.connect(
        user= 'root' , password = 'Dunggttn1512.', host='localhost', database='Student')
        mycursor = db.cursor()
        sql = "SELECT filename FROM fileupload WHERE id = %s" %(m)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        result_final.append(result)
        # result1=result[0]
        # result_final = json.dumps(result1)
        db.commit()
        db.close()    
        return result_final

    
    def show_all_data_from_information():

        db = mysql.connector.connect(
        user= 'root' , password = 'Dunggttn1512.', host='localhost', database='Student')
        mycursor = db.cursor()
        sql = "SELECT * FROM Information"
        mycursor.execute(sql)
        myresult = mycursor.fetchall()
        db.close()
        return myresult

    def delete_from_information_by_id (m) : 
        
        db = mysql.connector.connect(
        user= 'root' , password = 'Dunggttn1512.', host='localhost', database='Student')
        mycursor = db.cursor()
        sql = "DELETE FROM Information WHERE ID = %s" % (m)
        mycursor.execute(sql)
        db.commit()
        db.close()
    
    def select_from_information_by_id(m): 

        db = mysql.connector.connect(
        user= 'root' , password = 'Dunggttn1512.', host='localhost', database='Student')
        mycursor = db.cursor()
        sql = "SELECT * FROM Information WHERE ID = %s" %(m)
        mycursor.execute(sql)
        result = mycursor.fetchall()
        db.commit()
        db.close()
        return result 