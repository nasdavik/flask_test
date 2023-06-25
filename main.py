from flask import Flask

app: Flask = Flask(__name__)


@app.route('/')
def test():
    return "Hello my dear friends"


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000)
