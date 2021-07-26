from flask import jsonify, g
from app import db
from app.api import bp
from app.api.auth import basic_auth


@bp.route('/tokens', methods=['POST'])
@basic_auth.login_required
def get_token():
    token = g.current_user.get_jwt()
    db.session.commit()
    return jsonify({'token': token})
    # JWT 没办法回收（不需要 DELETE /tokens），只能等它过期，所以有效时间别设置太长
    # 装饰器 @basic_auth.login_required 将指示 Flask-HTTPAuth 验证身份，当通过 BasicAuth 验证后，
    # 才使用用户模型的 get_token() 方法来生成 token，数据库提交在生成 token 后发出，
    # 以确保 token 及其到期时间被写回到数据库