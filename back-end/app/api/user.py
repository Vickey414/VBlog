'''这是一个用户的Restful API的设计'''
from app.api import bp
from app import db
import re
from flask import request, jsonify, url_for
from app.models import User
from app.api.error import bad_request


@bp.route('/users', methods=['POST'])
def create_user():
    '''注册一个新的用户'''
    data = request.get_json()
    if not data:
        return bad_request('You must post JSON data')

    message = {}
    if 'username' not in data or not data.get('username', None):
        message['username'] = 'Please provide a valid username.'
    pattern = '^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]' \
              '{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$'
    if 'email' not in data or not re.match(pattern,data.get('email',None)):
        message['email'] = "Please provide a valid email address"
    if 'password' not in data or not data.get('password', None):
        message['password'] = 'Please provide a valid password.'

    if User.query.filter_by(username= data.get('username',None)).first():
        message['username'] = 'Please use a different username.'
    if User.query.filter_by(email=data.get('email', None)).first():
        message['email'] = 'Please use a different email address.'
    if message:
        return bad_request(message)

    user = User()
    user.from_dict(data, new_user=True)
    # os.environ['NO_PROXY'] = '423down.com'
    # proxies = {'http': None, 'https': None}
    db.session.add(user)
    db.session.commit()
    response = jsonify(user.to_dict())
    # 注册完成之后会调用User函数将信息转化成dict，然后用json转换为json格式返回给后端
    response.status_code = 201
    # HTTP协议要求201响应包含一个值为新资源的URL的location
    response.headers['Location'] = url_for('api.get_user', id = user.id)
    return response


@bp.route('/users', methods=['GET'])
def get_users():
    '''返回所有用户的集合'''
    pass


@bp.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    '''返回一个用户的信息'''
    return jsonify(User.query.get_or_404(id).to_dict())


@bp.route('/users/<int:id>',methods = ['PUT'])
def update_user(id):
    '''修改一个用户'''
    pass


@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    '''删除一个用户'''
    pass