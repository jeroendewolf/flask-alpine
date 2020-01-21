from flask import Flask
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/json1')
def helloJson1():
    jsonMsg = 'Hello JSON1!'
    return jsonify(jsonMsg)

@app.route('/xml')
def helloXml():
    xmlMsg = "Hello XML!"
    r = flask.make_response( xmlMsg )
    r.mimetype = 'application/xml'
    return r

@app.route('/html')
def helloHtml():
    htmlMsg = "<html><head></head><body>Hello HTML!</body></html>"
    r = flask.make_response( htmlMsg )
    r.mimetype = 'text/html'
    return r

@app.route('/json2')
def helloJson2():
    jsonMsg = "Hello JSON2!"
    r = flask.make_response( jsonMsg )
    r.mimetype = 'application/json'
    return r

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
