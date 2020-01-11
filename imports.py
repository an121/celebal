import csv
import MySQLdb

mydb = MySQLdb.connect(host='localhost',
    user='root',
    db='test')
cursor = mydb.cursor()

with open('dataset1.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    line_count = 0
    for row in csv_reader:
        if line_count >0:
            id=row[0].replace('\'','')
            cities=row[1].replace('\'','')
            pincode=row[2].replace('\'','')
            office=row[3].replace('\'','')
            query='insert into dataset1 values({},\'{}\',{},\'{}\')'.format(id,cities,pincode,office)
            print(query)
            cursor.execute(query)
        line_count +=1
#close the connection to the database.
mydb.commit()
cursor.close()
print ("Done")

