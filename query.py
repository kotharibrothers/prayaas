#!/usr/bin/python2

import os
import sqlite3

rootdir = os.path.dirname(os.path.abspath(__file__))


def connection(db_name):
	global c
	conn=sqlite3.connect(db_name)
	c=conn.cursor()

def user_query(column,userType,age="*",gender="*",geocountry="*",msntime="*",msnvisits="*"):
    for row in c.execute('''select {0} from user_info where userType={1} and age={2} and gender={3} and 
    	geocountry={4} and msntime={5} and msnvisits={6}'''.format(column,userType,age,gender,geocountry,msntime,msnvisits)):
        print row


def query_str(*userid):
	for  row in c.execute("select  query_string from queries where q_id in  {0} ". format(tuple(userid))):
		print row