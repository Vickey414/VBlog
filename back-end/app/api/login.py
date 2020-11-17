from flask import Flask, request, session, redirect, url_for, render_template, make_response, jsonify
from app.api import bp


@bp.route('/login', methods = ('GET', 'POST'))
def login():
    if request.method == 'POST':
        session['username'] = request.json.get('username')
        session['password'] = request.json.get('password')
        # 登陆成功，则跳转到index界面
        return jsonify({'code': 200, 'token': 1234})
        # 登陆失败，则跳到当前的login界面
    return render_template('login.html')


@bp.route('/index')
def index():
    # 如果用户和密码都存在，则跳转到index界面，登陆成功
    if 'username' in session and 'password' in session:
        return render_template('index.html')
    # 否则，则跳转到login界面
    return redirect(url_for('login'))


@bp.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('password', None)
    return redirect(url_for('login'))

