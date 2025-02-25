from flask import Flask
import os

app = Flask(__name__)

ENV = os.getenv("ENV", "local")

@app.route('/', methods=['GET'])
def home():
    return return f"<h1>Hello, this is {ENV} !!!</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)