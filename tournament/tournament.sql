-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

--Here the table with all of the players is created, it has a unique ID for each of them plus a name (not necessarily unique)

CREATE DATABASE tournament;
\c tournament

create table players (
	id serial primary key, 
	name text);

-- In the matches table we have a list of the winner and loser for all of the matches

create table matches (
	winners integer references players(ID), 
	losers integer references players(ID));

--The totalmatches table is necessary so that we can perform additional types of computations more efficiently in the SQL code if we ever need to 

create table totalmatches (
	id integer references players(ID), 
	total integer);	

