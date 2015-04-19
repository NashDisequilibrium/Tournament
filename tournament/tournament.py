#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    global DB
    DB = psycopg2.connect("dbname=tournament")
    global c
    c=DB.cursor()


def deleteMatches():
    """Remove all the match records from the database.

    You can see that it deletes the matches and then winners and totalmatches so everything is reset"""
	
    #DB = psycopg2.connect("dbname=tournament")
    connect()
    #c=DB.cursor()
    c.execute("DELETE FROM matches;")
    c.execute("DELETE FROM totalmatches;")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
	
    connect()
    c.execute("DELETE FROM players;")
    DB.commit()
    DB.close()

def countPlayers():
    """Returns the number of players currently registered.
    Uses the table for players to count number of players"""
    connect()
    c.execute("SELECT COUNT(*) AS num FROM players;")
    number_of_players = [row[0] for row in c.fetchall()]
    DB.close()
    return number_of_players[0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).  
    This puts the information both into the players table and also winners so that the person starting has zero number of wins"""

    connect()
    c.execute("INSERT INTO players(name) VALUES (%s)", (name,))
    c.execute("INSERT INTO totalmatches(total) VALUES (0);")
    DB.commit()
    DB.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    Does all of the actions within SQL code not with Python as it is faster this way"""

    connect()
    c.execute("SELECT players.id, players.name, count(matches.winners) as num, count(totalmatches.total) as number_of_matches FROM players LEFT JOIN matches ON players.id = matches.winners LEFT JOIN totalmatches ON players.id = totalmatches.total GROUP BY players.id ORDER BY num;")
    standings = c.fetchall()
    print standings
    DB.close()
    return standings

def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    Self explanatory"""

    connect()
    c.execute("INSERT INTO matches(winners, losers) VALUES (%s, %s)", (winner, loser))
    c.execute("INSERT INTO totalmatches(total) VALUES (%s)", (winner,))
    c.execute("INSERT INTO totalmatches(total) VALUES (%s)", (loser,))	
    DB.commit()
    DB.close()	
	
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
     """

    final_standings = [(element[0], element[1]) for element in playerStandings()]
    #The even and odd numbers will be used to assign each player with the closest to them using the zip method described below. 
    tournament_next_pairings = zip(final_standings[0::2], final_standings[1::2])
    """Zipping takes the first element of one list and puts it in a tuple with the corresponding element in the other list, for example "zip ([1,2],[3,4])" becomes "[(1,3), (2,4)]"
    For this we will use the even and odd numbers from each iteration. This will work no matter the scale of the tournament so that he code is completely scalable. Next we take 
    each of the pairs in tournament_next_pairings and pair them together for the next round which will then be returned as tuples in tuple_pairings.""" 
    tuple_pairings = [tuple(list(sum(next_pair, ()))) for next_pair in tournament_next_pairings]
    return tuple_pairings
	
	
