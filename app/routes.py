from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import User

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    father_name = request.form.get('Father Name', '')
    user = User(name=name, email=email, phone=phone, father_name= father_name)
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('index'))
