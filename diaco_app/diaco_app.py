from flask import Flask, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

def url_creator(restaurant_name):
    #edit restaurant name
    lower_restaurant = restaurant_name.lower()
    replace_restaurant = lower_restaurant.replace("'", "")
    restaurant=replace_restaurant.replace(" ", "-")
    #create URL. TODO: add some different cities
    url="https://www.yelp.com/biz/" + restaurant + "-new-york"
    return url

def grab_data(url, reviews=10):
    page = requests.get(url)
    if page.status_code == 200:
        yelp_data = BeautifulSoup(page.content, 'html.parser')
        all_revs = yelp_data.find_all("div", class_="review-content")
        review_lst = list()
        for each in all_revs:
            inner = BeautifulSoup(str(each), 'html.parser')
            review_lst.append(inner.find('p'))
        return review_lst[0:reviews]
    else:
        review_lst.append("Sorry but there was an error in retrieving the restaurant name."\
        "Are you sure you spelled it right?")
        return review_lst







@app.route("/")
def hello():
    return render_template('layout.html')

#@app.route("/<restaurant>", methods=[GET])
