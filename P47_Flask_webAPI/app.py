from models import db, Automobilis
from flask import Flask, jsonify
from serializers import AutoSchema
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# fizinės db prijungimas, configas
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///automobiliai.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# paleidžiam db
db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/")
def home():
    all_autos = Automobilis.query.all()
    duomenys_jsonui = [AutoSchema.model_validate(auto).model_dump() for auto in all_autos]
    return jsonify(duomenys_jsonui)


if __name__ == "__main__":
    app.run()
