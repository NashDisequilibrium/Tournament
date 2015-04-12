-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

create table players (id serial primary key, name text);

create table matches (winners integer references players(ID), losers integer references players(ID));

--create table winners (id integer references players, numberofwins integer);

--c.execute("SELECT players.id, players.name, count(matches.winners) as num, count(matches.winners) + count(matches.losers) as total FROM players LEFT JOIN matches ON players.id = matches.winners GROUP BY players.id ORDER BY num;")
