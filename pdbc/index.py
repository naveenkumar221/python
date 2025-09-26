#pdbc (Python data base connectivity.)
#to communicate the database from the pyhton
#check the sql by using the help('modules')

#pip 


import mysql.connector
from db import info

try:
    conn=mysql.connector.connect(**info)
#        info={
#     'user':'naveen',
#     'password':'Naveenkumar@4221',
#     'host':'localhost',
#     'port':3306
# })

    print("connection sucessfuly: ")
except:
    print(" not able to connect: ")
cursor=conn.cursor()
 
## to create database:

query='create database if not exists 10000coders_new'

cursor.execute(query)



#using /selecting database
# cursor.execute("create database 1muser")
cursor.execute('use 10000coders')

#creating a table with id,name,email,course,date

try:
    create_table="""create table if not exists students_new_1(
    id int auto_increment primary key,name varchar(100),email varchar(100),
    course varchar(100),joined_date date);"""

    cursor.execute(create_table)
    print("table created sucessfully")
except mysql.connector.errors.ProgrammingError as e :
     print(e)
    # print("something went wrong")
    

## inserting single data into the table 

# def insertsingleRow(data):
#         try:

#             insertdata= """ insert into students (name,email,course,joined_date) values (%s,%s,%s,%s)"""
#             cursor.execute(insertdata,data)
#             print("data inserted sucessfully")
#         except:
#             print("something went wrong ")

# insertsingleRow(("suresh","suresh@gamil.com","pfs","2025-09-11"))
# insertsingleRow(("akhil","akhil@gamil.com","pfs","2025-04-15"))



##inserting multiple rows  at a time 

# def insertmultipleRow(data):
#     try:
#         insertdata=""" insert into students (name,email,course,joined_date) values (%s,%s,%s,%s) """
#         cursor.executemany(insertdata,data)
#         print("data inserted")
#     except:
#         print("something went wrong ")

# insertmultipleRow([("raju","raju@gmail.com","pfs","2025-02-03"),
#             ("kumar","kumar@gmail.com","pfs","2025-04-09"),
#             ("uppe","uppe@gmail.com","pfs","2025-05-10")])


## selecting all the data using 

# def  getRecords():
#     try:
#           query='select * from students'
#           cursor.execute(query)
#           results=cursor.fetchall()
#           for i in results:
#                print(i)
#         #   print(results)
#     except:
#          print("error occured ")
# getRecords()


## using the where condition 
# def getRecodrsofSamecours():
#     try:
#         query="select * from students where id=9 "
#         cursor.execute(query)
#         result=cursor.fetchall()
#         for i in result:
#              print(i)
             
#         # print(result)
#     except:
#          print("something went wrong")
# getRecodrsofSamecours()


## get limited records 

# def getLimitedRecords(limit):
#     try:
#         query=""" select * from students limit %s """
#         cursor.execute(query,(limit,))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("something went wrong")
#     finally:
#         print("exuted sucessfully ")
# getLimitedRecords(5)



## using order by 

# def getLimitedRecords(limit):
#     try:
#         query=""" select * from students order by name asc limit %s """
#         cursor.execute(query,(limit,))
#         result=cursor.fetchall()
#         print(result)
#     except:
#         print("something went wrong")
#     finally:
#         print("exuted sucessfully ")
# getLimitedRecords(5)




## updating recorde with newemail

# def updateCoursebyEmail(course,email):
#     try:
#         query=""" update students set course = %s where email=%s """
#         cursor.execute(query,(course,email))
#         print("data updated sucessfully")
#     except:
#         print("something went wrong ")
# updateCoursebyEmail('JFS','naveen@gmail.com')


## updating both value using email

# def updateNameAndCourseByEmail(new_name,new_course,email):
#     try:
#         query=""" update students set name = %s,course = %s where email = %s"""
#         cursor.execute(query,(new_name,new_course,email))
#         print("data is update")
#     except:
#         print("something went wrong")
# updateNameAndCourseByEmail('akhila','JFS','newemail@example.com')

# def updateEmailOfStudent():
#     try:
#         new_email = "newemail@example.com"
#         student_id = 9  
#         query = "UPDATE students SET email = %s WHERE id = %s"
#         values = (new_email, student_id)
#         cursor.execute(query, values)  
#         print("Email updated successfully!")
#     except Exception as e:
#         print("Something went wrong:", e)
# updateEmailOfStudent()


## deleting the single record of email

# def deleteRecordByID(id):
#     try:
#         query = "DELETE FROM students WHERE id = %s"
#         cursor.execute(query, (id,))
#         print(f"Record with email {id} deleted successfully!")
#     except:
#         print("Something went wrong:")
# deleteRecordByID(5) 


# def deleteRecordByEmail(email):
#     try:
#         query="delete from students where email = %s"
#         cursor.execute(query,(email,))
#         print("deleted sucessfully")
#     except:
#         print("something went wrong")
# deleteRecordByEmail('raju@gmail.com')


## deletimg the multiple records using the name

# def deleteRecordsByName(name):
#     try:
#         query = "DELETE FROM students WHERE name = %s"
#         cursor.execute(query, (name,))
#         print(f"All records with name {name} deleted successfully!")
#     except Exception as e:
#         print("Something went wrong:", e)

# deleteRecordsByName('')














          




conn.commit()
cursor.close()
conn.close()


