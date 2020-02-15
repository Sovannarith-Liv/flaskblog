import os#The os. path module is always the path module suitable for the operating system Python is running on, and therefore usable for local paths
import secrets #use to generate random hex
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail


def save_picture(form_picture):
    random_hex = s.token_hex(8) #generate random hex for the picture name
    _, f_ext = os.path.splitext(form_picture.filename) # use to seperate the filename the it extension and use only the file extension 
    picture_fn = random_hex + f_ext # concatenate both random name that we create for the profile pic with the file extension that we just split.
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn) #app.root_path will give the root path of our application to the package directory

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)
    i.save(picture_path) #save i into picture_path

    return picture_fn


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@demo.com', #This is the default sender which will send the message to a particular recipients
                  recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link: 
{url_for('users.reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
''' #This statement is the body of the message which send to the recipients 
    mail.send(msg)