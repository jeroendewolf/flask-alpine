from flask import Flask
from flask import Response
from flask import jsonify
from fpdf import FPDF

app = Flask(__name__)

@app.route('/json1')
def helloJson1():
    jsonMsg = 'Hello JSON1!'
    return jsonify(jsonMsg)

@app.route('/xml')
def helloXml():
    xmlMsg = "<xml>Hello XML!</xml>"
    r = app.make_response( xmlMsg )
    r.mimetype = 'application/xml'
    return r

@app.route('/html')
def helloHtml():
    htmlMsg = "<html><head></head><body>Hello HTML!</body></html>"
    r = app.make_response( htmlMsg )
    r.mimetype = 'text/html'
    return r

@app.route('/json2')
def helloJson2():
    jsonMsg = "Hello JSON2!"
    r = app.make_response( jsonMsg )
    r.mimetype = 'application/json'
    return r

@app.route('/pdf')
def jpg_to_pdf():
    pdf = FPDF()
    pdf.add_page()
    pdf.image('wolf.jpg', 150, 150)
    response = app.make_response(pdf.output(dest='S').encode('latin-1'))
    response.headers.set('Content-Disposition', 'attachment', 'wolf.pdf')
    response.headers.set('Content-Type', 'application/pdf')
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
