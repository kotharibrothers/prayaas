import sqlite3
import time

f=open("/home/ank/prayaas/prayaas.db","wb")
f.close()
conn=sqlite3.connect("/home/ank/prayaas/prayaas.db")
c=conn.cursor()
start_time=time.time()
l=[]
count=0

c.execute('''CREATE TABLE tab_1
             (userId TEXT, 
             userType TEXT,
             age INT,
             gender TEXT,
             geocountry INT)''')


with open("/home/ank/prayaas/contestdata_0.txt") as myfile:

    for line in myfile:

        line=line.strip()
        data_list=line.split("\t")
        data=tuple(data_list[0:5]) #writing information of the user for inserting in table1
        write_list.append(data)

        if len(l) == 1000000 :
            c.executemany('INSERT INTO tab_1 VALUES (?,?,?,?,?)', write_list)
            conn.commit()
            count+=1;
            print count
            l=[]

conn.commit()
conn.close()
end_time=time.time()
elapsed=(end_time - start_time)
print elapsed
