from flask import Flask, render_template

app = Flask(__name__)

#Definir ruta padre
@app.route("/")
def index():
    return render_template("index.html")

#Crear otra ruta
@app.route("/personal")
def personal():
    return render_template("personal.html")

if __name__ == "__main__":
    app.run(debug=True)