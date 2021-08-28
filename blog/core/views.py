from flask import render_template, request, Blueprint
from blog.models import BlogPost, User
from flask_login import current_user
from datetime import datetime

core = Blueprint('core', __name__)

@core.route('/')
def index():

    page = request.args.get('page', 1, type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date1.desc()).paginate(page=page, per_page=3)
    return render_template('index.html', blog_posts=blog_posts)

@core.route('/info')
def info():

    return render_template('info.html')
