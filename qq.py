from flask import Flask

app = Flask(__name__)
# app.config['DEBUG'] = True


@app.route('/')
@app.route('/index')
def index():
    return "Привет, МИР!"


@app.route('/home', methods=['GET'])
def home():
    return '<h1>Home</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
