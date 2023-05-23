import mysql.connector

conn=mysql.connector.connect(host='127.0.0.1',user='root',password='root',database='table')
my_cursor=conn.cursor()

#my_cursor.execute("CREATE TABLE Internship (origin VARCHAR(30),destination VARCHAR(30),start_date date,end_date date,cost_per_kg FLOAT )")
#my_cursor.execute("DESCRIBE Details")
#sql=("INSERT INTO Internship (origin,destination,start_date,end_date,cost_per_kg) VALUES ('India','USA','2009-09-09','2014-09-04',200.87)")
#values=('India','USA',200.87)
#delete=("DELETE FROM Internship WHERE origin='India'")
#my_cursor.execute(delete)
cmd=("INSERT INTO Internship (origin,destination,start_date,end_date,cost_per_kg) VALUES (%s,%s,%s,%s,%s)")
value=[('India','USA','2009-09-09','2014-09-04',200.87),
       ('Chennai','Delhi','2015-09-07','2019-07-03',3000),
       ('Bombay','Kashmir','2007-09-06','2013-08-04',4389),
       ('Coimbatore','Chennai','2010-09-03','2016-09-05',5456),
       ('Kanyakumari','Bangalore','2016-06-02','2022-09-04',7678)]
my_cursor.executemany(cmd,value)

for x in my_cursor:
    print(x)
 
conn.commit()
conn.close()

print("Connection successfully created!")