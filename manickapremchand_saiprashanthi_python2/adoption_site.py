import os
from forms import AddForm, DelForm, AddOwnerForm
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
app = Flask(__name__)
# Key for Forms
app.config['SECRET_KEY'] = 'mysecretkey'

############################################

        # SQL DATABASE AND MODELS

##########################################
basedir = os.path.abspath(os.path.dirname(__file__))
# Old SQLite DB
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data.sqlite')

# New My SQL DB
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Manicka1983@localhost/puppy_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

class Puppy(db.Model):

    __tablename__ = 'puppies'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    eye_color = db.Column(db.Text)
    good_catcher = db.Column(db.Text)
    owner = db.relationship('Owner',backref='puppy',uselist=False)

    def __init__(self,name,eye_color, good_catcher):
        self.name = name
        self.eye_color = eye_color
        self.good_catcher = good_catcher



    def __repr__(self):

        if (self.good_catcher == "Yes"):
            isGoodCatcher = 'Good Catcher'
        else:
            isGoodCatcher = 'Not a Good Catcher'

        if self.owner:
            return f"Puppy name is {self.name} with eye color {self.eye_color} and is {isGoodCatcher} and owned by {self.owner.name}"
        else:
            return f"Puppy name is {self.name} and has no owner assigned yet."

class Owner(db.Model):

    __tablename__ = 'owners'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use puppies.id because __tablename__='puppies'
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))

    def __init__(self,name,puppy_id):
        self.name = name
        self.puppy_id = puppy_id

    def __repr__(self):
        return f"Owner Name: {self.name}"
############################################

        # VIEWS WITH FORMS

##########################################
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add', methods=['GET', 'POST'])
def add_pup():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        eye_color = form.eye_color.data
        good_catcher = form.good_catcher.data

        # Add new Puppy to database
        new_pup = Puppy(name , eye_color, good_catcher)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add.html',form=form)
@app.route('/add_owner', methods=['GET', 'POST'])
def add_owner():

    form = AddOwnerForm()

    if form.validate_on_submit():
        name = form.name.data
        pup_id = form.pup_id.data
        # Add new owner to database
        new_owner = Owner(name,pup_id)
        db.session.add(new_owner)
        db.session.commit()

        return redirect(url_for('list_pup'))

    return render_template('add_owner.html',form=form)

@app.route('/list')
def list_pup():
    # Grab a list of puppies from database.
    puppies = Puppy.query.all()
    return render_template('list.html', puppies=puppies)

@app.route('/delete', methods=['GET', 'POST'])
def del_pup():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('list_pup'))
    return render_template('delete.html',form=form)


if __name__ == '__main__':
    app.run(debug=True)
