# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL
# model the class after the friend table from our database

class Player:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.player_position = data['player_position']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('baseball_player').query_db(query)
        # Create an empty list to append our instances of friends
        players = []
        # Iterate over the db results and create instances of friends with cls.
        for player in results:
            players.append(cls(player))
        return players
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO players (first_name, last_name, player_position, created_at, updated_at) VALUES (%(first_name)s, %(last_name)s, %(player_position)s, NOW(), NOW());"
        result = connectToMySQL('baseball_player').query_db(query, data)
        return result
            
