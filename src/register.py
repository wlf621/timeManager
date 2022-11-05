import string

from flask import render_template, request, Blueprint
from sqlalchemy.orm import sessionmaker

from data import Base, engine
from src.login import User

Register = Blueprint('register', __name__, template_folder='../templates')


def check_passwd(passwd: string):
    flag1 = False
    flag2 = False
    flag3 = False

    for ch in passwd:
        if 'a' <= ch <= 'z':
            flag1 = True
        elif 'A' <= ch <= 'Z':
            flag2 = True
        elif '0' <= ch <= '9':
            flag3 = True
        else:
            return False

    return flag1 and flag2 and flag3


@Register.route('/register', methods=["GET", "POST"])
def register():
    context = {
    }
    datas = request.form
    if len(datas) == 0:
        return render_template('register.html', **context)

    user_name = datas.get("user_name")
    if len(user_name) == 0:
        context['result'] = '请输入用户名！'
        return render_template('register.html', **context)
    passwd = datas.get("password")
    repeat_passwd = datas.get("repeat_password")
    if passwd != repeat_passwd:
        context['result'] = '两次输入密码不一致！'
        return render_template('register.html', **context)
    if len(passwd) < 8:
        context['result'] = '密码过短！'
        return render_template('register.html', **context)
    if not check_passwd(passwd):
        context['result'] = '密码不符合规范！'
        return render_template('register.html', **context)

    # 查询数据库
    Base.metadata.create_all()
    Session = sessionmaker(bind=engine)
    session = Session()
    item = session.query(User).filter(User.user_name == user_name).one_or_none()
    if item is not None:
        context['result'] = '用户名已存在，注册失败'
        return render_template('register.html', **context)

    ed_user = User(user_name=user_name, passwd=passwd)
    session.add(ed_user)
    session.commit()

    context['result'] = '注册成功！'
    return render_template('login.html', **context)
