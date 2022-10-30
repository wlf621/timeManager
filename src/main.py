from flask import render_template
from app import app


@app.route('/')
def main():
    context = {
        "title": "时间管理",
        "time": "时间",
        "event": "事件",
        "submit": "提交"
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
