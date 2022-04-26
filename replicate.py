import csv
import mysql.connector
import pandas as pd
from mysql.connector import Error
mydb = mysql.connector.connect(host='localhost',
                                         database='btc',
                                         user='root',
                                         password='Trigma#2020')
cursor = mydb.cursor()
query = "Select * from BTC_DATA;"
df = pd.read_sql(query,mydb)
#csv_data = csv.reader(file('/home/kkr/Downloads/cypto/data.csv'))
with open('/home/kkr/Downloads/crypto/newdata/feature.csv', 'r') as file:
 csv_data = csv.reader(file)

 print('*'*20,csv_data)
# execute and insert the csv into the database.
 for row in csv_data:

        t = row[2]
        dff = df.loc[df['open_time'] == t]
        print(dff)
        raise
        if dff.empty:
         cursor.execute('INSERT INTO BTC_DATA(close,open,high,low,price,volume,datetime,delta,open_interest,TPivot,TR1,TS1,TR2,TS2,TR3,TS3,GGPivot,GGS1,GGS2,GGS3,GGR1,GGR2,GGR3,FBPivot,FBR1,FBR2,FBR3,FBS3,FBS2,FBS1,WPivot,WS1,WS2,WS3,WR1,WR2,WR3,vwap,bear_fractal,bull_fractal,symbol)''VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)',row)
         print("SUCCESSFULLY ADDED TO DB")
        else:
         print("ENTRY DISCARDED DUE TO REPLICATION")        
mydb.commit()

cursor.close()
