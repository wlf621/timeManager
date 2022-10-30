from flask import render_template

from app import app


@app.route('/test')
def test():
    return render_template('about.html')


@app.route('/')
def main():
    years = list(range(2022, 2100))
    months = list(range(1, 13))
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    hours = list(range(1, 25))

    context = {
        "title": "时间管理",
        "years": years,
        "months": months,
        "days": days,
        "hours": hours
    }

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
