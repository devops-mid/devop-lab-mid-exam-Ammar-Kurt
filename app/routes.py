from flask import render_template, request, redirect, url_for, flash
from app import app, db
from app.models import User
import re  # To use regular expressions for validation

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone', '')  # Optional field
    father_name = request.form.get('father_name', '')  # Make sure the field name matches the form

    # Server-side validation for email (checks if it's a valid email)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        flash("Invalid email address", "error")  # Flash an error message
        return redirect(url_for('index'))

    # Server-side validation for phone (must be numeric and 10 digits)
    if not phone.isdigit() or len(phone) != 10:
        flash("Phone number must be numeric and exactly 10 digits", "error")
        return redirect(url_for('index'))

    # Create a new user and save to the database
    user = User(name=name, email=email, phone=phone, father_name=father_name)
    db.session.add(user)
    db.session.commit()

    flash("Form submitted successfully", "success")  # Flash a success message
    return redirect(url_for('index'))

