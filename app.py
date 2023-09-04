import os

import openai
from flask import Flask, redirect, render_template, request, url_for
from utils import return_top_keywords

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        company_name = request.form['company_name']
        postion = request.form['postion']
        category = request.form['category']
        location = request.form['location']
        nof_employers = request.form['nof_employers']
        print(company_name)
        return redirect(url_for("index", result="okay"))
    result = request.args.get("result")
    return render_template("home.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')