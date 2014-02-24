#!/bin/bash

root_dir=$PWD

echo "
 ____                                  
|  _ \ _ __ __ _ _   _  __ _  __ _ ___ 
| |_) | '__/ _` | | | |/ _` |/ _` / __|
|  __/| | | (_| | |_| | (_| | (_| \__ \
|_|   |_|  \__,_|\__, |\__,_|\__,_|___/
                 |___/    
""

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

# Start the query process
	python query.py
else
	exit;
fi