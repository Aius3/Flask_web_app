from models import Automobilis, db
from app import app

with app.app_context():
    automobiliai = [
        Automobilis(gamintojas="Toyota", modelis="Corolla", spalva="Raudona", metai=2020, variklis="1.8L I4", kaina=15000),
        Automobilis(gamintojas="BMW", modelis="X5", spalva="Juoda", metai=2018, variklis="3.0L V6", kaina=50000),
        Automobilis(gamintojas="Tesla", modelis="Model 3", spalva="Balta", metai=2022, variklis="Elektrinis", kaina=30000),
        Automobilis(gamintojas="Ford", modelis="Focus", spalva="Mėlyna", metai=2015, variklis="2.0L I4", kaina=8000),
        Automobilis(gamintojas="Mercedes-Benz", modelis="S-Class", spalva="Sidabrinė", metai=2019, variklis="4.0L V8", kaina=70000),
    ]

    db.session.add_all(automobiliai)
    db.session.commit()
    print("Duomenys užpildyti")
