from flask import render_template, request, Blueprint, url_for, redirect
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from data import Base, engine

Login = Blueprint('login', __name__, template_folder='../templates')


class User(Base):
    # 定义表名为users
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    user_name = Column(String(20), primary_key=True)
    passwd = Column(String(20))


@Login.route('/', methods=['GET', 'POST'])
def login():
    context = {
    }
    datas = request.form
    if len(datas) == 0:
        return render_template('login.html', **context)

    user_name = datas.get("user_name")
    passwd = datas.get("password")

    # 查询数据库
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(User).filter(User.user_name == user_name).one_or_none()
    if item is None:
        context['result'] = '用户不存在，登陆失败！'
        return render_template('login.html', **context)
    if passwd != item.passwd:
        context['result'] = '密码错误！'
        return render_template('login.html', **context)
    if passwd == item.passwd:
        return redirect('index')
    return render_template('login.html', **context)
