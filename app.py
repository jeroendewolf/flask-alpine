from flask import Flask
from flask import Response
from flask import jsonify

app = Flask(__name__)

@app.route('/json1')
def helloJson():
    jsonmsg = 'Hello JSON!'
    return jsonify(jsonmsg)

@app.route('/xml')
def helloXml():
    xmlMsg = "Hello XML!"
    header("Content-type: text/xml")
    return xmlMsg

@app.route('/html')
df helloHtml():
    htmlMsg = "<html><head></head><body><input type="BUTTON" value="Hello HTML!"></body></html>"
    header("Content-type: text/xml")
    return htmlMsg

@app.route('/json2')
df helloHtml():
    htmlMsg = "Hello JSON2!"
    header("Content-type: application/json")
    return htmlMsg

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
