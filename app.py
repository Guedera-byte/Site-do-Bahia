from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/historia")
def historia():
    return render_template("historia.html")

@app.route("/titulos")
def titulos():
    return render_template("titulos.html")

@app.route("/elenco")
def elenco():
    return render_template("elenco.html")

if __name__ == "__main__":
    app.run(debug=True)