from flask import Flask

app = Flask(__name__)


@app.route('/user')
def index():
    """view function
    """
    return '<h1>Hello Lianrui</h1>'


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=80)
