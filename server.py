import os
import csv
from flask import Flask, render_template, send_from_directory, request, redirect

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def intro(name=None, occupation=None, desc=None):
    return render_template('index.html', name='Charles Robertson',
                           occupation='Python Developer',
                           description='Here to SERVE you!')


@app.route("/<path:webpage>")
def navigate(webpage):
    return render_template(webpage)


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               '/assets/apple-icon-180x180.png', mimetype='image/png')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return render_template('thankyou.html', email=data['email'])
        except:
            return 'Something went wrong :(...Nothing was saved to database.'


def write_to_csv(data: dict):
    with open("database.csv", mode="a", newline='') as db:
        csvreader = csv.DictWriter(db, fieldnames=data.keys())
        csvreader.writerow(data)
