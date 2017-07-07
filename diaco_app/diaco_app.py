from flask import Flask, render_template, url_for, request
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
        star_div = yelp_data.find("div", class_="rating-info clearfix").find('img')
        review_lst = [star_div.get('alt', '')]
        for each in all_revs:
            inner = BeautifulSoup(str(each), 'html.parser')
            review_lst.append(inner.find('p').get_text())
    else:
        review_lst = ["Error: Sorry but there was an error in retrieving the restaurant name."\
        "Are you sure you spelled it right?"]
    return review_lst[0:int(reviews)]


@app.route("/")
def homepage():
    return render_template('layout.html')

@app.route("/result", methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        reviews = request.form['reviews']
        restaurant = request.form['restaurant']
        url = url_creator(restaurant)
        result = (restaurant, grab_data(url, int(reviews)))
        return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)
