# My Diaco take home test app! 

## Caveats

Thanks so much for the opportunity to put this together! It was genuinely a fun project and I am 
really, really excited to talk to Dia & Co!! I want to take a quick moment to add a few caveats here:
So when Gem told me about this project she gave me a time limit of four hours to complete. 
I have attempted to work within this constraint and as such I am sending you this app without testing,error catching, or style sheets (all stuff I would normally add!). This app was completed in four hours on July 6, 2017. 

#### So here is what I was tasked to complete: 
>Build a web page that accepts the name of a pizza restaurant in New York and displays the n most recent Yelp reviews for this >restaurant, where n is a user input (assume n < 10).
>The web page should also display the average score (0-5) of the relevant reviews
>Implementation:
>Your code should be written in Python.
>Feel free to use any Python packages/frameworks (e.g., Flask, Django) that you deem helpful.
>Yelp’s API does not support retrieving reviews, so you will have to scrape the data yourself.

So to complete this I utilized python 3.6 and FLASK for most of the work with BeautifulSoup used to scrape YELP. 
So- to get this up and running please do the following: 

1. Clone the repo to your local directory and navigate to the diaco_app directory of the project (diaco_app folder)
2. _If you want to_ go ahead and activate the virtualenv with `source bin/activate`
3. Assuming you have python 3.6 installed go ahead and `pip install -r requirements.txt`
4. While still in the root directory of the project you will need to alter your FLASK_APP environment variable so:
	*`export FLASK_APP=diaco_app.py` and then `flask run`

	*At this point you should see the message saying that the app is running.
5. Navigate to http://127.0.0.1:5000 (or localhost:5000) in a browser and you should see the home screen
6. Enter the required information: restaurant name and number of reviews.
7. Please enter *both* parameters (I have not yet added error checking to these- so if any field is blank it fails)
8. You should get the results page

Please contact me at "fernpombeiro@yahoo.com" with any questions, comments, or concerns. Thanks!!
