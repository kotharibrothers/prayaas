import sqlite3
import time
 
start_time = time.clock()
 
conn = sqlite3.connect('prayaas.db')
c = conn.cursor()
 
c.execute('''CREATE TABLE user_info (id TEXT, user_type TEXT, age INT, gender TEXT, geo TEXT)''')
c.execute('''CREATE TABLE domain_mapper (user TEXT, domain INT, count INT, FOREIGN KEY(user) REFRENCES user_info(id)''')
c.execute('''CREATE TABLE search_data ())
lines, counts = 0

 
with open("contestdata_0.txt", "rb") as test:
    for line in test:
    columns = line.strip().split(" ")

 
conn.commit()
conn.close()
 
elapsed_time = time.clock() - start_time
print "Time elapsed: {} seconds".format(elapsed_time)
print "Read {} lines".format(lines)