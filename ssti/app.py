#!/usr/bin/python3.10
from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/sub", methods=['POST'])
def sub():
    username = request.form['username']
    return render_template_string(f"""
    <html>
    <h1> thanks for subscribing {username}
    </html>
    """)


if __name__ == "__main__":
    app.run()
