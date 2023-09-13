from player_app.config.mysqlconnection import connectToMySQL

class Team:
    def __init__(self, data):
        self.id = data['id']
        self.team_name = data['team_name']
        self.city = data['city']
        self.ballpark = data['ballpark']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    def full_team_name(self):
        return f"{self.city} {self.team_name}"

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM teams;"
        results = connectToMySQL('baseball_player').query_db(query)
        teams = []
        for t in results:
            teams.append( cls(t) )
        return teams

    @classmethod
    def save(cls, data):
        query = "INSERT INTO teams (team_name, city, ballpark) VALUES (%(team_name)s,%(city)s,%(ballpark)s);"
        result = connectToMySQL('baseball_player').query_db(query,data)
        return result

    @classmethod
    def get_one (cls, data):
        query="SELECT * FROM teams WHERE id = %(id)s;"
        result = connectToMySQL('baseball_player').query_db(query,data)
        return cls(result[0])

    @classmethod
    def update(cls,data):
        query = "UPDATE teams SET team_name=%(team_name)s, ballpark=%(ballpark)s, city=%(city)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('baseball_player').query_db(query,data)

    @classmethod
    def destroy(cls,data):
        query  = "DELETE FROM teams WHERE id = %(id)s;"
        return connectToMySQL('baseball_player').query_db(query,data)