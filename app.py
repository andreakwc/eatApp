from flask import Flask, jsonify, render_template, request
import requests
import gdata.spreadsheet.service
import gdata.spreadsheet
import gdata.service
import atom.service
import getopt
import sys
import re, os, os.path
import string

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/hello")
def hello():
 	return "Hey There! Hello World!"

# def __init__(self, email, password):
# 	self.gd_client = gdata.spreadsheet.service.SpreadsheetsService()
# 	self.gd_client.email = eatApp2015@gmail.com
# 	self.gd_client.password = dining2015
# 	self.gd_client.source = "eatApp"
# 	self.gd_client.ProgrammaticLogin()
	#self.curr_key = ""
	#self.curr_wksht_id = ""
	#self.list_feed = None

#@app.route("/search/<search_query>")
#def search(search_query):	
#	return search_query

# @app.route("/select", methods=["GET", "POST"])
# def search():
# 	if request.method == "POST":
# 		url = "https://docs.google.com/spreadsheet/ccc?key=0At7RkuwrpNM0dDNfNGd5STk2TXQ1aHZ2elNqUFVIM0E&usp=drive_web&pli=1#gid=0" + request.form["user_search"]
# 		response_dict = requests.get(url).json()
# 		return jsonify(response_dict)
# 	else:
# 		return render_template("search.html")

@app.route("/select", methods = ["GET", "POST"])
def select():
	if request.method == "POST":
		#url = "https://docs.google.com/spreadsheet/ccc?key=0At7RkuwrpNM0dDNfNGd5STk2TXQ1aHZ2elNqUFVIM0E&usp=drive_web&pli=1#gid=0"
		where = request.form["Where"]
		what = request.form["What"]
		query_string = "&tq=select%20A%20where%20B%20contains%20" + where + "%20and%20C%20contains%20" + what
		#wholeQuery = url + query_string
		#response_dict = requests.get(wholeQuery).json()
		
		gd_client = gdata.spreadsheet.service.SpreadsheetsService()
		gd_client.email = "chan.andreakw@gmail.com"
		gd_client.password = "imgoodthanks"
		gd_client.source = "eatApp"
		gd_client.ProgrammaticLogin()

		key = "0At7RkuwrpNM0dDNfNGd5STk2TXQ1aHZ2elNqUFVIM0E"
		wksht_id = "0"

		q = gdata.spreadsheet.service.ListQuery()
		#q.orderby = "column:Name"
		#q.reverse = "true"

		feed = gd_client.GetListFeed(key, wksht_id, query=q)

		for row_entry in feed.entry:
			record = gdata.spreadsheet.text_db.Record(row_entry=row_entry)
		print "%s" % (record.content["Name"])

		return whole_Query
	else:
		return render_template("search.html")


@app.errorhandler(404)
def page_not_found(error):
	return "Sorry, this page was not found", 404

@app.route("/search/exception")
def exception():
	return "Gotcha!"

if __name__ == "__main__":
	app.run(host="0.0.0.0")
