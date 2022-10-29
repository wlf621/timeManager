from flask import Flask, jsonify

app = Flask(__name__)


# url 路径
@app.route('/')
def hello_world():
    return {"hello":"伦飞!"}


if __name__ == '__main__':
    #app.debug = True
    app.config.from_pyfile('./config.conf', silent=True)
    app.run()
