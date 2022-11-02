from flask import render_template, request, Blueprint
from sqlalchemy import create_engine

data_page = Blueprint('data_page', __name__, template_folder='../templates')

# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'timeManager'
USERNAME = 'root'
PASSWORD = 'wanwan621x'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# 创建数据库引擎
engine = create_engine(DB_URI)


@data_page.route('/result', methods=["POST"])
def read_data():
    context = {
        "result": "失败"
    }
    datas = request.form
    context["year"] = datas.get("year")
    context["month"] = datas.get("month")
    context["day"] = datas.get("day")
    context["hour"] = datas.get("hour")
    context["event"] = str(datas.get("event"))
    context["type"] = str(datas.get("type"))

    with engine.connect() as con:
        sql = f'''INSERT INTO test ( year, month, day, hours, type, event) VALUES({context["year"]}, {context["month"]},\
{context["day"]}, {context["hour"]}, '{context["type"]}', '{context["event"]}'); '''
        rs = con.execute(sql)
        print(rs.rowcount)

    context["result"] = "成功"
    return render_template('result.html', **context)

