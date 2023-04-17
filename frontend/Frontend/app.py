import os
from flask import Flask, render_template, send_file, request, send_from_directory
import requests
from pydantic import BaseModel


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("Home.html")

@app.route('/Home.html')
def home_path():
    return render_template("Home.html")

@app.route('/CalElectic.html')
def CalElectic():
    return render_template("CalElectic.html")

@app.route('/CalAir.html')
def CalAir():
    return render_template("CalAir.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port="8081")