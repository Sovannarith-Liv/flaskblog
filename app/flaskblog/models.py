from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app 
from flaskblog import db, login_manager, app # we import app in order to use app secret_key
from flask_login import UserMixin

"""This method use to reload the user object from the user ID that store in the session. it take the unicode ID of a user and return the coresponding user object"""
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True) # each of the user need to have the unique id and primary_key will provide each every user with the unique id
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='default.jpg') #profile of the user
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True) #create the relationship between Post and User model.
    # backref='author' will give us the author of the user who post a particular post, Lazy=True: to specify that the sqlalchemy will load the data from the database.
    #by the purpose of this statement, is to get the post from the user. 

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8') #user_id is the payload of the token

    @staticmethod
    def verify_reset_token(token): #This method is a static method which it not require to hae self paramenter.
        s = Serializer(current_app.config['SECRET_KEY']) #current_app will the create_app method in __init__.py file
        try:
            user_id = s.loads(token)['user_id'] # This statement will return the id of the user with a particular token
        except:
            return None
        return User.query.get(user_id)
        

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')" #use to display data when we using query method to access data from database
        


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Use to specify the user in the post model 

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"