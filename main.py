from flask import Flask, render_template, request, abort

app: Flask = Flask(__name__)

news: dict = {}


@app.route('/', methods=['get', 'post'])
def index():
    if request.method == 'POST':
        if request.form.get('title') and request.form.get('content'):
            news[request.form.get('title')] = request.form.get('content')
            return render_template('index.html', news=news)
        abort(404)


if __name__ == '__main__':
    app.run(host="127.0.0.1", port=5000, debug=True)
