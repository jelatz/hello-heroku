from flask import Flask
app = Flask(__name__)

@app.route('/')
def index();
  return 'This is my Application! Jojie Lad M. Lanete BSIT-II'
