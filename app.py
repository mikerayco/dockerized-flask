from flask import Flask
app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello! This is a Flask app running in a container!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')