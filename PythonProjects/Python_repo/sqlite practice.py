import sqlite3
import sys

arguments = sys.argv

if arguments[0] == "-c" :
    mode = "cli"
else:
    mode = "gui"

con = sqlite3.connect("TasksDB.db")
cursor = con.cursor()
cursor.execute("""CREATE TABLE if not exists tasks (
                                id integer primary key autoincrement,
                                taskname text not null,
                                taskdesc text,
                                taskstatus text not null
)""")
print ("tasks table was created successfully !")

cursor.execute(""" insert into tasks (taskname, taskdesc, taskstatus) values ("Buy Items", "Curd, Milk, Bread", "False")""")
print("Task was added successfully")

con.commit()

cursor.execute(" select * from tasks ")

rows = cursor.fetchall()

for row in rows:
    print (row)