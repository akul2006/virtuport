from website import create_app
from flask import render_template, Flask, Blueprint

app = create_app()

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True, port=5000)
