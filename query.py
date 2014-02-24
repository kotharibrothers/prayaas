#!/usr/bin/python2

import os
import sqlite3
import time

rootdir = os.path.dirname(os.path.abspath(__file__))

start_time = time.clock()

conn = sqlite3.connect(os.path.join(rootdir, 'prayaas.db'))
c = conn.cursor()

with c:
	cur.execute('''SELECT * FROM user_info WHERE (userID = ?) OR 
		(userType = ? AND age = ? AND gender = ? AND geocountry AND msntime = ? AND msnvisits = ?), () ''')        
    con.commit()


conn.close()

elapsed_time = time.clock() - start_time
print "Time elapsed: {} seconds".format(elapsed_time)
print "Read {} lines".format(lines)