from flask import Flask, request

app = Flask(__name__)
# app.config['DEBUG'] = True

posts = []

@app.route('/')
@app.route('/index')
def index():
    return "Привет, МИР!"


@app.route('/feed', methods=['GET'])
def feed():
    if posts:
        return '<br>'.join(posts)
    return '<h1>Тут пусто</h1>'


@app.route('/add_post', methods=['GET'])
def add_post():
    post = str(request.query_string).replase('%20', ' ')[2:-1]
    posts.append(post)
    return post


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
