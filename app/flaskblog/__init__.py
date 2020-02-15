from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt 
from flask_login import LoginManager # LoginManager contain the code that let our application and flask-login work together. 
from flask_mail import Mail # imported this package inside this file in order to do the configuration on it
from flaskblog.config import Config 

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy() # here we just create an object for that class 
bcrypt = Bcrypt()
login_manager = LoginManager()  
login_manager.login_view = 'users.login' # (login: is the route of login page) This statement will direct the user to the login page and flask a message when the user attempt to enter the login_required page and haven't login yet
login_manager.login_message_category = 'info' #The message category to flash when a user is redirected to the login page. 
"""When the log in view is redirected to, it will have a next variable in the query string, which is the page that the user was trying to access. Alternatively, 
if USE_SESSION_FOR_NEXT is True, the page is stored in the session under the key next."""

mail = Mail()

def create_app(config_class=Config):
    
    db.init_app(app) # here we do the initialization for that object.
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    from flaskblog.users.routes import users # users, posts, main are all the object of it blueprint 
    from flaskblog.posts.routes import posts
    from flaskblog.main.routes import main
    from flaskblog.errors.handlers import errors
    app.register_blueprint(users)
    app.register_blueprint(posts)
    app.register_blueprint(main)
    app.register_blueprint(errors)

    return app