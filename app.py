from flask import Flask
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/json1')
def helloJson1():
    jsonmsg = 'Hello JSON!'
    return jsonify(jsonmsg)

@app.route('/xml')
def helloXml():
    xmlMsg = "Hello XML!"
    header("Content-type: text/xml")
    return xmlMsg

@app.route('/html')
def helloHtml():
    htmlMsg = "<html><head></head><body>Hello HTML!</body></html>"
    header("Content-type: text/html")
    return htmlMsg

@app.route('/json2')
def helloJson2():
    htmlMsg = "Hello JSON2!"
    header("Content-type: application/json")
    return htmlMsg

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
