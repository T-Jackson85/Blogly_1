from flask_sqlalchemy import SQLAlchemy 

db = SQLAlchemy()

DEFAULT_IMAGE_URL=" https://upload.wikimedia.org/wikipedia/commons/thumb/a/ac/No_image_available.svg/300px-No_image_available.svg.png"


"""Models for Blogly."""

class Users(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, 
                   primary_key=True,
                   autoincrement=True)
    
    name = db.Column(db.text(30),
                     nullable=False,
                     unique=True)
    
    imgUrl = db.Column(db.text(max),
                       nullable=False,
                       default= DEFAULT_IMAGE_URL
                       )
    @property
    def full_name(self):

        return f"{self.first_name} {self.last_name}"
    
    

def connect_db(app):
    """connects database to flask app"""
    
    db.app = app
    db.init_app(app)