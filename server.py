from flask import Flask, render_template

app = Flask(__name__)


@app.get("/")
def index():
    return render_template("index.html")


@app.get("/ceva")
def ceva():
    return render_template("ceva.html")


@app.get("/altceva")
def altceva():
    return render_template("altceva.html")


@app.get("/altceva/<int:id>")
def incaceva(id):
    lista = ['ala', 'bala', 'portocala']
    # lista = []
    return render_template("incaceva.html", id=id, lista=lista)


if __name__ == "__main__":
    app.run(debug=True)
