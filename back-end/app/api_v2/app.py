from flask import Blueprint
from flask_restful import Api

bp = Blueprint('api_v2',__name__)

#初始化rest API
api = Api(bp)

#统一注册路由
