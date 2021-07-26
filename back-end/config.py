'''这是一个配置文件'''
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')

# sql_uri = 'mysql+pymysql://root:vickey@127.0.0.1:3306/VickeyBlog'


class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = "mysql://root:vickey@localhost:3306/VickeyBlog"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
