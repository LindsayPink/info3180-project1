from . import db

class Profile(db.Model):
    __tablename__ = 'profiles'

    userid = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_on = db.Column(db.Date)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(255), unique=True)
    location = db.Column(db.String(80))
    bio = db.Column(db.String(255))
    photo = db.Column(db.String(255))
    
    def __init__(self, created_on, firstname, lastname, gender, email, location, bio, photo):
        self.created_on = created_on
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.bio = bio
        self.photo = photo
        
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        try:
            return unicode(self.id)
        except NameError:
            return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.username)
