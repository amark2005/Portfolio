from flask import Flask, render_template
import requests
import json
app=Flask(__name__, static_folder="/portfolio/style.css")
@app.route('/')
def index():
    return render_template("home.html")
app.run(host="0.0.0.0",port=5002,debug=True)