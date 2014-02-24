Prayaas, Technex'14, Indian Institute of Technology(BHU), Varanasi
----------

**Prayaas** is an event based on building database systems that can scale and handle *big data* using efficient methods. 

In this implementation, **Python** is used with **SQLite3** providing high-speed querying and efficient, robust read and write operations.

SQLite3 was chosen because of 
- its high scalability(high volume size upto 140TB!), 
- lowest querying times, 
- cross-platform compatibility,
- compact size of the database
- inbuilt Python support
- and zero config headaches :)

The benchmarks for SQLite3 can be seen here:

![BS Img]

More info on SQLite @ <http://sqlite.org>


Version
----------
0.1


Setup
----------

Put the domain-mapping.csv file and the raw text files containg data in the same directory before using.

A install script is provided with this package. Open a terminal session and type:
```
chmod +x install.sh
./install.sh

```

After that a prayaas.db file is created.
Do the following:

```
python write.py #for setting up the sqlite3 database

```
The above script will  load up the database required for querying and  will display time of setup on exit.
It will also count on execution of every million of line in the text file.
After that for querying use the following command in the current directory:
```
sqlite3 prayaas.db

```
A  sqlite3 prompt will appear and you can execute your raw sql queries.

Database Structure
----------

The event problem statement provided 4 raw, text files (each upto 1GB in size). The text files contained ***tab-delimited*** MSN user data in the form of:

- userID, 
- userType(Machine or Human), 
- age, 
- gender(Unknown, Male, Female), 
- country, 
- domain seaches 
- and specific search keywords.
- domain names corresponding to index numbers given to them

Here separate tables were created for user_info, domain mapping and search queries. Each table contained a foreignkey related the specific data in relation to userID (aliased with ROWID of SQLite). 


Usage
----------

Here are some of the sample queries you can do at the SQLite shell:
```
$ sqlite> select rowid from user_info where (gender = 'M') and ( age between 25 and 35 ) and (msnvisits > 0) and (geocountry = 'US');

$ sqlite> select query_string from queries where id in ( select rowid from user_info where (gender = 'M') and ( age between 25 and 35 ) and (msnvisits > 0) and (geocountry = 'US'));

```

For simple queries, use the query module provided. 

Contributors
----------

[Viyat Bhalodia](https://github.com/delta24)

[Ankush Sharma](https://github.com/black_perl)


TODO
----------

Future versions will see the use of the ***pandas*** library for data analysis, efficient algorithms for data crunching, and support for ***regex*** matching and searching.


Contributions
----------

Submit bug reports @ [GitHub Issue Tracker](https://github.com/delta24/prayaas/issues)

Send us a pull request! 

[BS Img]: http://i.imgur.com/gPCCdLF.png
