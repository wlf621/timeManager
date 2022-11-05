import json

from flask import render_template, request
from data import data_page
from app import app
from data import engine
from login import Login
from register import Register


@app.route('/test')
def test():
    return render_template('about.html')


def show_oneday():
    return render_template('show.html')


@app.route('/index')
def main():
    years = list(range(2022, 2100))
    months = list(range(1, 13))
    days = list(range(1, 32))
    hours = list(range(1, 25))
    types = ['交通', '工作', '学习', '娱乐']
    types_cnt = {'交通': 0, '工作': 0, '学习': 0, '娱乐': 0}

    context = {
        "title": "时间管理",
        "years": years,
        "months": months,
        "days": days,
        "hours": hours,
        "types": types
    }

    # 图表，待优化
    datas = request.args
    if len(datas) != 0:
        year = int(datas.get("show_year"))
        month = int(datas.get("show_month"))
        day = int(datas.get("show_day"))
        with engine.connect() as con:
            sql = f'''select event_type from test where `year`={year} and `month`={month} and `day`={day};'''
            type_items = con.execute(sql).fetchall()
            for item in type_items:
                if item[0] in types_cnt:
                    types_cnt[item[0]] = types_cnt[item[0]] + 1

    context["data"] = json.dumps(types_cnt)

    return render_template('index.html', **context)


if __name__ == '__main__':
    app.register_blueprint(data_page)
    app.register_blueprint(Login)
    app.register_blueprint(Register)

    app.run(host='127.0.0.1', port=5000)
