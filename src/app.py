from flask import Flask

app = Flask(__name__, template_folder='../templates')
app.config.from_pyfile('./config.conf', silent=True)
