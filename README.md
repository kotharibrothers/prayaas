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

A install script is provided with this package. Open a terminal session and type:
```
chmod +x install.sh
./install.sh

```

Put the domain-mapping.csv file and the raw text files in the same directory before using

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
