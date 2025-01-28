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
    search_text = request.args.get("searchlaukelis")
    if search_text:
        automobiliai = Automobilis.query.filter(Automobilis.gamintojas.ilike(f"{search_text}%")).all()
    else:
        automobiliai = Automobilis.query.all()
    return render_template('index.html', automobiliai=automobiliai, search_text=search_text)

    
@app.route("/automobilis/<int:row_id>")
def one_auto(row_id):
    automobilis = Automobilis.query.get(row_id)
    if automobilis:
        return render_template("one_auto.html", automobilis=automobilis)
    else:
        return f"Automobilis su id {row_id} neegzistuoja"


@app.route("/automobilis/redaguoti/<int:row_id>", methods=["get", "post"])
def update_auto(row_id):
    automobilis = Automobilis.query.get(row_id)
    if not automobilis:
        return f"Automobilis su id {row_id} neegzistuoja"

    if request.method == "GET":
        # Return the form with the existing data
        return render_template("update_auto_form.html", automobilis=automobilis)

    elif request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        metai = request.form.get("metailaukelis")
        variklis = request.form.get("variklislaukelis")
        kaina = request.form.get("kainalaukelis")
        automobilis.gamintojas = gamintojas
        automobilis.modelis = modelis
        automobilis.spalva = spalva
        automobilis.metai = metai
        automobilis.variklis = variklis
        automobilis.kaina = kaina
        db.session.commit()
        return redirect(url_for("home"))  # nukreipimas į home funkcijos endpointą
        # return redirect(f"/automobilis/{row_id}")  # variantas nukreipimo į vieno projekto rodymą


@app.route("/automobilis/trynimas/<int:row_id>", methods=["POST"])
def delete_auto(row_id):
    automobilis = Automobilis.query.get(row_id)
    if not automobilis:
        return f"Automobilis su id {row_id} neegzistuoja"
    else:
        db.session.delete(automobilis)
        db.session.commit()
    return redirect(url_for("home"))


@app.route("/automobilis/naujas", methods=["GET", "POST"])
def create_auto():
    if request.method == "GET":
        return render_template("create_auto_form.html")
    if request.method == "POST":
        gamintojas = request.form.get("gamintojaslaukelis")
        modelis = request.form.get("modelislaukelis")
        spalva = request.form.get("spalvalaukelis")
        metai = request.form.get("metailaukelis")
        variklis = request.form.get("variklislaukelis")
        kaina = request.form.get("kainalaukelis")
        if gamintojas and modelis and spalva and metai and variklis and kaina:
            new_auto = Automobilis(gamintojas=gamintojas, modelis=modelis, spalva=spalva, metai=metai, variklis=variklis, kaina=kaina,)
            db.session.add(new_auto)
            db.session.commit()
        return redirect(url_for('home'))
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
