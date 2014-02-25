#!/usr/bin/python2

import os
import sqlite3
import time
import csv
import sys

rootdir = os.path.dirname(os.path.abspath(__file__))

# Remove before submitting
f=open(os.path.join(rootdir,'prayaas.db'),"wb")
f.close()

conn = sqlite3.connect(os.path.join(rootdir,'prayaas.db'))
conn.text_factory = str
c = conn.cursor()
start_time = time.time()
user_info_list = []
domain_data_list = []
user_id = 1
queries_data_list=[]
count=1

c.execute('''CREATE TABLE user_info
            (id INT PRIMARY KEY,
            userId TEXT, 
            userType TEXT,
            age INT,
            gender TEXT,
            geocountry TEXT,
            msntime INT,
            msnvisits INT
            )''')#creating table for the userinfo

c.execute('''CREATE TABLE queries
            (q_id INT,
            query_string TEXT,
            count INT,
            FOREIGN KEY(q_id) REFERENCES user_info(rowid) 
            )''')
#foreign key references at the last and best way for addind m2m rel is creating a seperate mapping table

c.execute('''CREATE TABLE domains
            (d_id INT,
            domain_code TEXT,
            count INT,
            FOREIGN KEY(d_id) REFERENCES user_info(rowid)
            )''')

c.execute('''CREATE TABLE domain_mapper
            (domain_code TEXT,
            domain_name TEXT
            )''')



with open(os.path.join(rootdir, 'DomainMapping.csv'), 'rb') as fin: 
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(fin) # comma is default delimiter
    to_db= [ ( str(i['\xef\xbb\xbfDomainId']), str(i['Name']) ) for i in dr]#getting the csv values from the dictionary object 
    c.executemany("INSERT INTO domain_mapper (domain_code, domain_name) VALUES (?, ?)", to_db )
    conn.commit()


with open(os.path.join(rootdir,"contestdata_0.txt")) as myfile:

    for line in myfile:

        line = line.strip()
        data_list = line.split("\t")
        
        user_info_data = tuple(data_list[0:5]+data_list[7:]) #writing information of the user for inserting in table1
        user_info_list.append(user_info_data)
       
        if data_list[5] != "" :
            domain_data = data_list[5].split("|")
            for m in domain_data:
                domain_data_list.append((user_id,m.split(";")[0],m.split(";")[1]))

        if data_list[6] != "" :
            queries_data = data_list[6].split("|")
            for m in queries_data:
                queries_data_list.append((user_id,m.split(";")[0],m.split(";")[1]))


        if len(user_info_list) == 1000000 :

            c.executemany('INSERT INTO user_info (userId,userType,age,gender,geocountry,msntime,msnvisits) \
            VALUES (?,?,?,?,?,?,?)',user_info_list)
            conn.commit()

            c.executemany('INSERT INTO domains VALUES (?,?,?)', domain_data_list)
            c.executemany('INSERT INTO queries VALUES (?,?,?)', queries_data_list)
            conn.commit()
           
            print count
            count+=1
            user_info_list=[]
            domain_data_list=[]
            queries_data_list=[]

        user_id+=1;


#recording the remaining
c.executemany('INSERT INTO user_info (userId,userType,age,gender,geocountry,msntime,msnvisits) \
            VALUES (?,?,?,?,?,?,?)',user_info_list)
conn.commit()

c.executemany('INSERT INTO domains VALUES (?,?,?)', domain_data_list)
c.executemany('INSERT INTO queries VALUES (?,?,?)', queries_data_list)
conn.commit()            

conn.close() #closing the connection

#### Time ####
end_time=time.time()
elapsed=(end_time - start_time)
print elapsed

sys.exit(1)
