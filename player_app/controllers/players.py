from flask import render_template, request, redirect

from player_app import app
from player_app.models.player import Player

@app.route('/')
def index():
    return redirect('/players')

@app.route('/players')
def players():
    return render_template("players.html",players=Player.get_all())

@app.route('/player/new')
def new_player():
    return render_template("new.html")

@app.route('/player/create',methods=['POST'])
def create_player():
    print(request.form)
    Player.save(request.form)
    return redirect('/players')

@app.route('/player/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit.html", player=Player.get_one(data))

@app.route('/player/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("show.html", player=Player.get_one(data))

@app.route('/player/update',methods=['POST'])
def update():
    Player.update(request.form)
    return redirect('/players')

@app.route('/player/destroy/<int:id>')
def destroy(id):
    data ={
        'id': id
    }
    Player.destroy(data)
    return redirect('/players')