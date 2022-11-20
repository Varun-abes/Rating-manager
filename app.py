from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail


app = Flask(__name__)

ENV = 'dev'
if(ENV == 'dev'):
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:\mvlziwyxdligvw:a7bf26f0f8050b11eff16c176a7fc7e7aee0633e06e71736c16aa34ea0f246d5@ec2-3-219-135-162.compute-1.amazonaws.com:5432\der69nsvob6bas'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:\mvlziwyxdligvw:a7bf26f0f8050b11eff16c176a7fc7e7aee0633e06e71736c16aa34ea0f246d5@ec2-3-219-135-162.compute-1.amazonaws.com:5432\der69nsvob6bas'
    
    
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
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