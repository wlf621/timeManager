from flask import render_template, request, Blueprint
from sqlalchemy import create_engine, Integer, Column, String
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

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
Base = declarative_base(engine)


class Test(Base):
    # 定义表名为users
    __tablename__ = 'test'

    # 将id设置为主键，并且默认是自增长的
    index = Column(Integer, primary_key=True)
    year = Column(Integer)
    month = Column(Integer)
    day = Column(Integer)
    hour = Column(Integer)
    event_type = Column(String(20))
    event = Column(String(100))

    # 让打印出来的数据更好看，可选的
    def __repr__(self):
        return "<test(index='%s',year='%s',month='%s',day='%s',hour='%s',event_type='%s',event='%s')>" % (
            self.index, self.year, self.month, self.day, self.hour, self.event_type, self.event)


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

    # 数据库操作
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    session = Session()

    row_data = Test(year=context["year"], month=context["month"], day=context["day"], hour=context["hour"],
                    event_type=context["type"], event=context["event"])
    session.add(row_data)
    session.commit()

    context["result"] = "成功"
    return render_template('result.html', **context)


def data_test():
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    # 或者
    # Session = sessionmaker()
    # Session.configure(bind=engine)
    session = Session()

    for instance in session.query(Test).order_by(Test.index):
        print(instance)


if __name__ == '__main__':
    data_test()
