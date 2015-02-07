from flask import Flask, jsonify, render_template, url_for, request
import requests
import sys
import json
import urllib
import urllib2
import pprint

app = Flask(__name__)
app.config["DEBUG"] = True

#yelp stuff
CONSUMER_KEY = 'qispYO7ID1yGKTlg04lTUg'
CONSUMER_SECRET = 'zgRquIhrRen0P_Ri1JMSaE64hx0'
TOKEN = '57qDhDaZvfWo32UWXra3qpxPd9ZS3zpq'
TOKEN_SECRET = 'ILOgsb0q8ecfIdVAK_oz'

API_HOST = 'api.yelp.com'
DEFAULT_LOCATION = 'New York, NY'
SEARCH_PATH = '/v2/search/'
BUSINESS_PATH = '/v2/business/'
SEARCH_LIMIT = 3

@app.route("/hello")
def hello():
    return "Hey There! Hello World!"

# def __init__(self, email, password):
#   self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
#   self.gd_client.email = eatApp2015@gmail.com
#   self.gd_client.password = dining2015
#   self.gd_client.source = "eatApp"
#   self.gd_client.ProgrammaticLogin()
    #self.curr_key = ""
    #self.curr_wksht_id = ""
    #self.list_feed = None

#@app.route("/search/<search_query>")
#def search(search_query):  
#   return search_query

# @app.route("/select", methods=["GET", "POST"])
# def search():
#   if request.method == "POST":
#       url = "https://docs.google.com/spreadsheet/ccc?key=0At7RkuwrpNM0dDNfNGd5STk2TXQ1aHZ2elNqUFVIM0E&usp=drive_web&pli=1#gid=0" + request.form["user_search"]
#       response_dict = requests.get(url).json()
#       return jsonify(response_dict)
#   else:
#       return render_template("search.html")


# @app.route("/select", methods = ["GET", "POST"])
# def select():
#     if request.method == "POST":
#         where = request.form["Where"]
#         what = request.form["What"]
#         places = []

#         with open('static/js/restaurants.json') as json_file:
#             restaurants = json.loads(json_file.read())["restaurants"]
#             for r in restaurants:
#                 if r['Area'] == where and r['Cuisine'] == what:
#                     places.append(r['Name'])
#         return render_template("results.html", elements = places)
#     return render_template("search.html")

@app.route("/results", methods = ["GET", "POST"])
def results():
    if request.method == "POST":
        where = request.form["Where"]
        what = request.form["What"]
        places = []

        with open('static/js/restaurants.json') as json_file:
            restaurants = json.loads(json_file.read())["restaurants"]
            for r in restaurants:
                if r['Area'] == where and r['Cuisine'] == what:
                    places.append(r['Name'])
        return render_template("results.html", elements = places)
    return render_template("results.html")

@app.errorhandler(404)
def page_not_found(error):
    return "Sorry, this page was not found", 404

@app.route("/search/exception")
def exception():
    return "Gotcha!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
