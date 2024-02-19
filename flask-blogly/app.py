"""Blogly application."""

from flask import Flask, request, redirect, render_template
from models import db, connect_db, Users


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True


connect_db(app)
db.create_all()

@app.route("/")
def home():
    """Homepage shows list of all users"""

    return redirect("/users")

@app.route('/users')
def user_list():
    """Shows user info"""

    users= Users.query.order_by(Users.last_name, Users.first_name).all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=["GET"])
def users_new_form():

    return render_template('users/new.html')

@app.route('/users/new', methods=["POST"])
def new_users():

    new_user= Users(
        first_name= request.form['first_name'],
        last_name= request.form['last_name'],
        image_url= request.form['image-url'] or None)
    
    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')

@app.route('/users/<int:users_id>')
def show_user(users_id):

    users = Users.query.get_or_404(users_id)
    return render_template('users/show.html', users=users)

@app.route('/users/<int:users_id>/edit', methods=["POST"])
def users_update(users_id):

    user = Users.query.get_or_404(users_id)
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.image = request.form['image_url']

    db.session.add(user)
    db.session.commit()

    return redirect("/users")

if __name__== "__main__":
     app.run(debug=True)
