#!/bin/bash

root_dir=$PWD

CORRECT="y"
echo "This will setup up the database and preconfigure some settings. Continue(y/n)?"
read OPTION
if [ "$OPTION" == "$CORRECT" ]; then 

#### First setup sqlite3 database ####
	echo "Creating a sqlite database named 'prayaas.db':"
	touch prayaas.db
	echo "Created successfully!"

### Make the .py file executable ###
	chmod +x *.py

else
	exit;
fi
