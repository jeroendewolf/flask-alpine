from flask import Flask
from flask import Response

app = Flask(__name__)

@app.route('/')
def hello():

    xml = 'foo'
    return Response(xml, mimetype='text/xml')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
