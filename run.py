# create the virtual environment
# python -m venv venv
# source venv/bin/activate  # On Windows: venv\Scripts\activate
# pip install -r requirements.txt

# Install Required Packages
# pip install flask flask-sqlalchemy flask-wtf flask-migrate email-validator

# pip freeze > requirements.txt

# Verify Flask Environment Variables
# set FLASK_APP=run.py      # Windows

# run app
# python run.py
#  or
# flask run


from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
