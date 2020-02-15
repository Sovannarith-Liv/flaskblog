import os

class Config: 
	SECRET_KEY = '5791628bb0b13ce0c676dfde280ba245'
	SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
	MAIL_SERVER = 'smtp.googlemail.com' # This is the domain of the google mail server. 
	MAIL_PORT = 587 # This is the port number of google mail server.
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('EMAIL_USER') # The email which we use to access the mail server of google 
	MAIL_PASSWORD = os.environ.get('EMAIL_PASS') # This is the password of the email.