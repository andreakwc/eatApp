from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/hello")
def hello():
 	return "Hello World!"

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
		url = "https://docs.google.com/spreadsheet/ccc?key=0At7RkuwrpNM0dDNfNGd5STk2TXQ1aHZ2elNqUFVIM0E&usp=drive_web&pli=1#gid=0"
		where = request.form["Where"]
		what = request.form["What"]
		query_string = "&tq=select%20A%20where%20B%20contains%20" + where + "%20and%20C%20contains%20" + what
		wholeQuery = url + query_string
		response_dict = requests.get(wholeQuery)
		return response_dict
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
