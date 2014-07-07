import mysql.connector as sql

## connect with database
con = sql.connect(user='root', password='root',host='127.0.0.1',database='turn_server')
cursor = con.cursor()

## insert in to database
query_insert = ("insert into state(uuid,available) values('shdkffsdjsdhjhsdvfjsdvfhsdf',1);")
cursor.execute(query_insert)
query_insert = ("insert into state(uuid,available) values('shdkffsdjsdhjhfgshgjhgjhsaf',1);")
cursor.execute(query_insert)
## select from the database
query_search = ("select * from state;")
cursor.execute(query_search)
for value in cursor:
    print value#format(value)
## delete from the database
#query_delete = ("delete from state;")
#cursor.execute(query_delete)
con.commit()

