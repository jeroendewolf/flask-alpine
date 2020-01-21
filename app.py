from flask import Flask
from flask import Response
from flask import jsonify


app = Flask(__name__)

@app.route('/')
def hello():

    jsonmsg = 'foo bar'
    return jsonify(jsonmsg)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
