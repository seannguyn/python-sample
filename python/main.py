from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "<h1>hello this is a test!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)