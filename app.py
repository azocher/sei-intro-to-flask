from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello, World!"

@app.route('/r/<subreddit>')
def sub_find(subreddit):
    return "Welcome to the {} subreddit!".format(subreddit)

@app.route('/multiply/<int:num1>/<int:num2>')
def multiply(num1, num2):
    result = num1 * num2
    return str(result)

@app.route('/hello/<word>')
def hello(name):
    return render_template("index.html", name=name)