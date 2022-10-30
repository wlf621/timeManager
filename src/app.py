from flask import Flask

app = Flask(__name__, template_folder='../templates', static_folder='../static', static_url_path='')
app.config.from_pyfile('./config.py', silent=True)
