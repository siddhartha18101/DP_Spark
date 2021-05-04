from flask import Flask, render_template, request

import os

from flask import Flask, flash, request, redirect, url_for, send_from_directory,send_file
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'up_folder'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app = Flask(__name__)

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




# class Feedback(db.Model):
#     __tablename__ = 'feedback'
#     id = db.Column(db.Integer, primary_key=True)
#     customer = db.Column(db.String(200), unique=True)
#     dealer = db.Column(db.String(200))
#     rating = db.Column(db.Integer)
#     comments = db.Column(db.Text())

#     def __init__(self, customer, dealer, rating, comments):
#         self.customer = customer
#         self.dealer = dealer
#         self.rating = rating
#         self.comments = comments

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download')
def download_file():
    up="Bd_assignment_2.pdf"
    return send_file(up, as_attachment=True)

@app.route('/submit', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files["file"]
        upld_name=file.filename
        file.save(os.path.join("up_folder", file.filename))
        print("FIle saved")
    return redirect('/final/'+upld_name)


@app.route('/final/<filename>')
def sendfile(filename):
    uploads = "up_folder/"+filename
    return send_file(uploads, as_attachment=True)
    


if __name__ == '__main__':
    app.secret_key = 'the random string'
    app.run()