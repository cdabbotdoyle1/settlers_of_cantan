from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Settlers of Catalan"

if __name__ == "__main__":
    app.run(debug=True, ssl_context=('cert.pem', 'key.pem'))