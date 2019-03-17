import os
from app import app, db
from flask import render_template, request, redirect, url_for, flash
from .forms import User
from .models import Profile
from werkzeug.utils import secure_filename
import datetime

rootdir = os.getcwd()
print (rootdir)

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')

@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html', name='Mary Jane')
    
@app.route('/profile', methods=['POST', 'GET'])
def profile():
    """Render the website's about page."""
    nUser = User()
    def bio_length(bio):
        if len(bio) > 255:
            flash('Bio too long. No more than 255 characters please.', 'danger')
            return False
        else:
            return True
    
    def uniqueEmail(email):
        if (Profile.query.filter_by(email=email).first()):
            flash(u'Email address taken.', 'danger')
            return False
        else:
            return True
        
    if request.method == 'POST':
        if nUser.validate_on_submit() and bio_length(nUser.bio.data) and uniqueEmail(nUser.email.data):
            created_on = datetime.datetime.today() #.strftime('Joined on %B %d, %Y')
            firstname = nUser.firstname.data
            lastname = nUser.lastname.data
            gender = nUser.gender.data
            email = nUser.email.data
            location = nUser.location.data
            bio = nUser.bio.data
            photo = nUser.photo.data

            filename = secure_filename(photo.filename)
            photo.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            
            newUser = Profile(created_on, firstname, lastname, gender, email, location, bio, filename)
            db.session.add(newUser)
            db.session.commit()
            
            flash('Profile successfully added!', 'success')
            return redirect(url_for('profiles'))
        flash_errors(nUser)
    return render_template("new-user.html", form=nUser)

@app.route('/profiles')
def profiles():
    """Render the page showing all users."""
    allUsers = Profile.query.order_by(Profile.userid).all()
    return render_template('profiles.html', users=allUsers)
    
@app.route('/profile/<int:userid>', methods=['GET'])
def user(userid):
    """Render page for a specified user."""
    user = Profile.query.filter_by(userid=userid).first()
    if user is not None:
        return render_template('user.html', user=user, joined=format_date_joined(user.created_on))
    return render_template('404.html')

def format_date_joined(date):
    return date.strftime("Joined on %B %d, %Y")

###
# The functions below should be applicable to all Flask apps.
###

# Flash errors from the form if validation fails
def flash_errors(form):
    for field, errors in form.errors.items():
        for error in errors:
            flash(u"Error in the %s field - %s" % (
                getattr(form, field).label.text,error), 'danger')

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
