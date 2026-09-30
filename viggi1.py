#create a database through python ....
import mysql.connector
def createdb() :
    try:
        
         con=mysql.connector.connect(
         host="127.0.0.1",
         port=3306,
         user="root",
         password="root",
         ssl_disable=True
         use_pure=True)

         cur=con.cursor()
        cd="create database mystudent"
        cur.execute(cd)
        con.commit()
        print ("database created successfully...")
        #print("2. my sql connection successful !")
        con.close()
        #print("3.connection closed.")

        except Exception as e:
            #print("4.conection failed:")
            #print(type(e).__name__)
            print(str(e))
#main
createdatabase()
    
                                    
                                    
