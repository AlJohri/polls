from polls.scrapers import RCPCurrent, HPCurrent
import os, threading

from flask import Flask
# from flask.ext.cors import cross_origin
from flask.ext.cors import cross_origin
app = Flask(__name__)

@app.after_request
@cross_origin("*") # allow all origins all methods everywhere in the app
def after(response):
	return response

@app.route("/rcp")
def rcp():
    t = threading.Thread(name="rcp", target=RCPCurrent.download, args=())
    t.start()
    return "started"

@app.route("/hp")
def hp():
    t = threading.Thread(name="hp", target=HPCurrent.download, args=())
    t.start()
    return "started"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 5000)), debug=True)
