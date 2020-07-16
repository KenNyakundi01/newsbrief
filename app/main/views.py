from flask import render_template,request,redirect,url_for
from . import main
#from requests import get_news, search_news
from .forms import ReviewForm
from ..models import Review
#Review = review.Review
    # Views
#@main.route('/')
#def index():
@main.route('/news/<int:id>')
def news(id):
    news = get_news(id)
    title = f'{news.title}'
    reviews = Review.get_reviews(news.id)
    return render_template('news.html',title = title,news = news,reviews = reviews)

