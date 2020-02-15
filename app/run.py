from flaskblog import create_app

app = create_app()

if __name__ == '__main__': # call the create_app method in __init__.py file and store the return value in app variable.
    app.run(debug=True)








