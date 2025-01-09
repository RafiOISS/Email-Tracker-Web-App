from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Country(db.Model):
    name = db.Column(db.String(100), primary_key=True)

    def __repr__(self):
        return f"<Country {self.name}>"

class University(db.Model):
    name = db.Column(db.String(200), primary_key=True)
    country = db.Column(db.String(100), db.ForeignKey('country.name'), nullable=False)
    application_deadline = db.Column(db.Date)
    website = db.Column(db.String(300))

    def __repr__(self):
        return f"<University {self.name}>"

class Professor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    university = db.Column(db.String(200), db.ForeignKey('university.name'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    interests = db.Column(db.String(300))
    profile = db.Column(db.String(300))

    def __repr__(self):
        return f"<Professor {self.name}>"

class Documents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    university = db.Column(db.String(200), db.ForeignKey('university.name'), nullable=False)
    application = db.Column(db.String(200))
    transcript = db.Column(db.String(200))
    cv = db.Column(db.String(200))

    def __repr__(self):
        return f"<Documents for {self.university}>"

class Mail(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    professor = db.Column(db.Integer, db.ForeignKey('professor.id'), nullable=False)
    draft = db.Column(db.Boolean, default=False)
    sent = db.Column(db.Boolean, default=False)
    response = db.Column(db.String(300), nullable=True)
    interview = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Mail to {self.professor}>"
