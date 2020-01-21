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
    return Response(xmlMsg, mimetype='text/xml')

@app.route('/html')
def helloHtml():
    htmlMsg = "<html><head></head><body>Hello HTML!</body></html>"
    return Response(htmlMsg, mimetype='text/html')

@app.route('/json2')
def helloJson2():
    jsonMsg = "Hello JSON2!"
    return Response(jsonMsg, mimetype='application/json')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
