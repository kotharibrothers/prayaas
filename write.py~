import sqlite3
import time

f=open("/home/ank/prayaas/prayaas.db","wb")
f.close()
conn=sqlite3.connect("/home/ank/prayaas/prayaas.db")
c=conn.cursor()
start_time=time.time()
write_list=[]
count=0

c.execute('''CREATE TABLE user_info
             (id INT PRIMARY KEY,
             userId TEXT, 
             userType TEXT,
             age INT,
             gender TEXT,
             geocountry TEXT)''')


with open("/home/ank/prayaas/contestdata_0.txt") as myfile:

    for line in myfile:

        line=line.strip()
        data_list=line.split("\t")
        data=tuple(data_list[0:5]) #writing information of the user for inserting in table1
        write_list.append(data)

        if len(write_list) == 1000000 :
            c.executemany('INSERT INTO user_info (userId,userType,age,gender,geocountry) VALUES (?,?,?,?,?)', write_list)
            conn.commit()
            count+=1;
            print count
            write_list=[]

conn.commit()
conn.close()
end_time=time.time()
elapsed=(end_time - start_time)
print elapsed
