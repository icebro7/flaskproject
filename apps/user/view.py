import string
import random

from flask import Blueprint, request, jsonify
from sendCode import sendcode
from flask import render_template
from werkzeug.security import generate_password_hash, check_password_hash

from databaseHandler import DatabaseEmployHandler

from apps.user.models import User, Code
from exts import db

user_bp = Blueprint('user', __name__)


# 门户页面
@user_bp.route('/')
def home_page():
    return render_template("homePage.html")


# 图表展示页面
@user_bp.route('/showPage')
def showPage():
    return render_template("showPage.html")


# 登录页面
@user_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        phone = request.form.get('phone')
        password = request.form.get('password')
        # 查询
        user_list = User.query.filter(User.phone == phone)

        for user in user_list:
            # 加密密码与输入密码的匹配
            flag = check_password_hash(user.password, password)
            if flag:
                username = user.username
                return render_template("showPage.html", username=username)
        else:
            return render_template('login.html', msg='用户名或者密码有误！')
    return render_template("login.html")


# 注册页面
@user_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        phone = request.form.get('phone')
        phonecode = request.form.get('phonecode')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        proof_code = Code.query.filter(Code.phonecode == phonecode).all()
        if password1 == password2 and len(proof_code) >= 1:
            # 前后密码一致， 验证码一致，创建用户
            user = User()
            user.username = username
            user.phone = phone
            user.phonecode = phonecode
            user.password = generate_password_hash(password1)
            db.session.add(user)
            db.session.commit()

            username = user.username
            return render_template("showPage.html",username=username)
        else:
            return render_template("register.html", msg='两个密码不同或验证码有误，再试试')
    return render_template("register.html")


# 手机号码验证
@user_bp.route('/checkphone', methods=['GET', 'POST'])
def check_phone():
    phone = request.args.get('phone')
    user = User.query.filter(User.phone == phone).all()
    # code: 400 不能用    200: 可以用
    if len(user) > 0:
        return jsonify(code=400, msg='此号码已被注册')
    else:
        return jsonify(code=200, msg='此号码可用')


# 发送验证码
@user_bp.route('/sendcode')
def send_code():
    # 随机验证码（数字）
    phone_code = string.digits
    phone_code = random.sample(phone_code, 5)
    captcha = ''.join(phone_code)

    # 存储验证码
    code = Code()
    code.phonecode = captcha
    db.session.add(code)
    db.session.commit()

    # 获取手机号码
    phone = request.args.get('phone')

    # 发送验证码
    send = sendcode.send(phone, captcha)

    # 判断是否发送成功，返回信息
    if send is not None:
        if send['status'] == 'OK':
            print('发送成功')
            return jsonify(code=200, phonemsg='信息已下发，注意查收')
        else:
            print('发送失败')
            return jsonify(code=400, phonemsg='信息发送失败，检查后再试')
    else:
        print('发送失败')
        return jsonify(code=400, phonemsg='信息发送失败，检查后再试')


# 以下皆为图表创建
@user_bp.route('/chart1')
def chart1():
    data = DatabaseEmployHandler().getSalaryMax()
    return render_template("chart1.html", result=data)


@user_bp.route('/chart2')
def chart2():
    return render_template("chart2.html")


@user_bp.route('/chart3')
def chart3():
    return render_template("chart3.html")


@user_bp.route('/chart4')
def chart4():
    return render_template("chart4.html")


@user_bp.route('/chart5')
def chart5():
    return render_template("chart5.html")


@user_bp.route('/chart6')
def chart6():
    return render_template("chart6.html")


@user_bp.route('/chart7')
def chart7():
    return render_template("chart7.html")
