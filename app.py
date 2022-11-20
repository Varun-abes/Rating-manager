from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail
from flask_migrate import Migrate


app = Flask(__name__)

ENV = 'dev'
if(ENV == 'dev'):
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rating_manager_user:EbX7uBmGSBVVMTVgZndh5ckMLyMyIslP@dpg-cdsthjpa6gdu24906vfg-a.oregon-postgres.render.com/rating_manager'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rating_manager_user:EbX7uBmGSBVVMTVgZndh5ckMLyMyIslP@dpg-cdsthjpa6gdu24906vfg-a.oregon-postgres.render.com/rating_manager'
    
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
migrate = Migrate(app, db)
app.app_context().push()


class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(100), unique=True)
    seller = db.Column(db.String(100))
    rate = db.Column(db.Integer)
    comment = db.Column(db.Text())
    
    
    def __init__(self,customer,seller,rate, comment):
        self.customer = customer
        self.seller =seller
        self.rate = rate
        self.comment = comment

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        seller = request.form['seller']
        rate = request.form['rate']
        comment = request.form['comment']
        if(customer == '' or seller == ''):
            return render_template('index.html', message= 'Please enter all fields!!!')
        
        # if customer does not exist
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer,seller,rate,comment)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, seller, rate, comment)
            return render_template('success.html')
        return render_template('index.html', message= 'Alredy submitted feedback !!!')



if __name__ == '__main__':
    app.run()