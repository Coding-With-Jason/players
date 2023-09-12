from player_app.config.mysqlconnection import connectToMySQL

class Player:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.player_position = data['player_position']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL('baseball_player').query_db(query)
        players = []
        for x in results:
            players.append( cls(x) )
        return players

    @classmethod
    def save(cls, data):
        query = "INSERT INTO players (first_name,last_name, player_position) VALUES (%(first_name)s,%(last_name)s,%(player_position)s);"
        result = connectToMySQL('baseball_player').query_db(query,data)
        return result

    @classmethod
    def get_one (cls, data):
        query="SELECT * FROM players WHERE id = %(id)s;"
        result = connectToMySQL('baseball_player').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE players SET first_name=%(first_name)s,last_name=%(last_name)s,player_position=%(player_position)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('baseball_player').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM players WHERE id = %(id)s;"
        return connectToMySQL('baseball_player').query_db(query,data)