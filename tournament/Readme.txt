Tournament Using Swiss Pairings
-------------------------------

Requirements:
-------------

VirtualBox
Vagrant
Git
Python 2.7.6
PostgreSQL 9.3.5
psycopg2


Files Included: 
---------------

tournament.py
tournament_test.py
tournament.sql


Instructions:
--------------

Open the Git Shell
Run vagrant from the appropriate folder ("vagrant up" and then "vagrant ssh")
Start PostgreSQL and then create the database "tournament" ("CREATE DATABASE tournament;"). 
Run tournament.sql which will input the SQL schema
Run tournament_test.py from the tournament folder


Notes:
-------

The tournament_test.py will delete the contents of the tables before doing a test, so this does not have to be done manually.
You can enter further names and other information into tournament_test.py to test larger structures. 
