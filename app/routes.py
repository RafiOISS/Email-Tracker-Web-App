from flask import Flask, render_template, request, jsonify, redirect, url_for, Blueprint
from app.models import db, Country, University, Professor, Documents, Mail

app = Blueprint('main', __name__)

@app.route('/')
def home():
    return render_template('dashboard.html')

@app.route('/add', methods=['GET', 'POST'])
def add_data():
    if request.method == 'POST':
        try:
            # Example: Adding a country
            country_name = request.form.get('country')
            new_country = Country(name=country_name)
            db.session.add(new_country)
            db.session.commit()
            return redirect(url_for('home'))
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {str(e)}", 500
    return render_template('add_data.html')

@app.route('/api/data', methods=['GET'])
def get_data():
    country = request.args.get('country')
    if country:
        universities = University.query.filter_by(country=country).all()
    else:
        universities = University.query.all()

    return jsonify([{
        'name': uni.name,
        'country': uni.country,
        'application_deadline': uni.application_deadline,
        'website': uni.website
    } for uni in universities])
