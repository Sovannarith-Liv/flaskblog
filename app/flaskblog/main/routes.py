from flask import render_template, request, Blueprint
from flaskblog.models import Post


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int) #This statement is to get the page number the default page is 1. 
    posts = Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5) #date_posted.desc(): sort the post descending with the date that it have been posted. 
    return render_template('home.html', posts=posts)


@main.route("/about")
def about():
    return render_template('about.html', title='About')
