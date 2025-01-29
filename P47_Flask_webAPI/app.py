from models import db, Automobilis
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# fizinės db prijungimas, configas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# paleidžiam db
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_cars = Automobilis.query.all()
    duomenys_jsonui = []
    for car in all_cars
        car_dict = {

        }


if __name__ == "__main__":
    app.run()
