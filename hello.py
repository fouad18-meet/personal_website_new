from flask import Flask, render_template, request , redirect, url_for, session
app = Flask(__name__)
app.secret_key="this is my project"

from flask_sqlalchemy import SQLAlchemy
 
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/website.db'
 
db = SQLAlchemy(app)
 
class Users(db.Model):
    __tablename__="users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    email=db.Column('email', db.Unicode)
    comment = db.Column('comment', db.Unicode)
 
 
db.create_all()





#YOUR WEB APP CODE GOES HERE


@app.route('/')
def main():
	return render_template('index.html')


@app.route('/contact', methods=['POST', 'GET'])
def contact():
    if(request.method == 'GET'):
        return render_template('contact.html')
    else:
        name = request.form['name']
        email = request.form['email']
        comment = request.form['comment']
        newUser = Users(name=name, email=email, comment=comment)
        db.session.add(newUser)
        db.session.commit()
	return render_template('contact.html')




@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/restaurants')
def restaurants():
    return render_template('restaurants.html')


















"""if __name__ == '__main__':
	app.run(debug=True)"""





