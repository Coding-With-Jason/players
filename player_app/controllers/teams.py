from flask import render_template, request, redirect

from player_app import app
from player_app.models.team import Team

# @app.route('/')
# def index():
#     return redirect('/players')

@app.route('/teams')
def teams():
    return render_template("teams.html",teams=Team.get_all())

@app.route('/team/new')
def new_team():
    return render_template("newteam.html")

@app.route('/team/create',methods=['POST'])
def create_team():
    print(request.form)
    Team.save(request.form)
    return redirect('/players')

@app.route('/team/edit/<int:id>')
def edit_team(id):
    data ={ 
        "id":id
    }
    return render_template("editteam.html", team=Team.get_one(data))

@app.route('/team/show/<int:id>')
def show_team(id):
    data ={ 
        "id":id
    }
    return render_template("showteam.html", team=Team.get_one(data))

@app.route('/team/update',methods=['POST'])
def update_team():
    Team.update(request.form)
    return redirect('/teams')

@app.route('/team/destroy/<int:id>')
def destroy_team(id):
    data ={
        'id': id
    }
    Team.destroy(data)
    return redirect('/teams')