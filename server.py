from flask import Flask, render_template, request, redirect

from player import Player

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/players')

@app.route('/players')
def users():
    return render_template("index.html", players = Player.get_all())

@app.route('/player/new')
def new():
    return render_template("new_player.html")

@app.route('/player/create', methods=['POST'])
def create():
    print(request.form)
    Player.save(request.form)
    return redirect('/players')

# @app.route("/")
# def index():
#     players = Player.get_all()
#     print(players)
#     return render_template("index.html", all_players = players)

# @app.route('/create_player', methods=["POST"])
# def create_player():
#     data = {
#         "fname": request.form["fname"],
#         "lname": request.form["lname"],
#         "player_position": request.form["player_position"]
#     }

#     Player.save(data)

#     return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)