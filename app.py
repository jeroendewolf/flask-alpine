from flask import Flask
from flask import Response

app = Flask(__name__)
ip = '0.0.0.0'

@app.route('/')
def hello():

    return 'Hello KPN!'

if __name__ == "__main__":
    app.run(host=ip, debug=False)
