from flask import Flask, render_template, url_for, request
from bs4 import BeautifulSoup
import statistics
import requests

app = Flask(__name__)

def url_creator(restaurant_name):
    #edit restaurant name
    lower_restaurant = restaurant_name.lower()
    replace_restaurant = lower_restaurant.replace("'", "")
    restaurant=replace_restaurant.replace(" ", "-")
    #create URL. Order by most recent per instructions
    url="https://www.yelp.com/biz/" + restaurant + "-new-york?sort_by=date_desc"
    return url

def grab_data(url, reviews=10):
    page = requests.get(url)
    if page.status_code == 200:
        yelp_data = BeautifulSoup(page.content, 'html.parser')
        all_revs = yelp_data.find_all("div", class_="review-content")
        review_lst = list()
        stars = list()
        for each in all_revs:
            inner = BeautifulSoup(str(each), 'html.parser')
            review_lst.append(inner.find('p').get_text())
            rev_num = int(inner.find('img').get('alt')[:1])
            stars.append(rev_num)
    else:
        review_lst = ["Error: Sorry but there was an error in retrieving the restaurant name."\
        "Are you sure you spelled it right?"]
    return review_lst[0:int(reviews)], stars[0:int(reviews)]


@app.route("/")
def homepage():
    return render_template('layout.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        reviews = request.form['reviews']
        restaurant = request.form['restaurant']
        url = url_creator(restaurant)
        reviews, stars = grab_data(url, int(reviews))
        result = (restaurant, reviews, statistics.mean(stars), len(stars))
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
