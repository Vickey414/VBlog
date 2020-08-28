'''这是一个配置文件'''
# basedir = os.path.abspath(os.path.dirname(__file__))
# #os.path.abspath返回绝对路径,两个一起使用返回的是.py文件的绝对路径
# load_dotenv(os.path.join(basedir, '.env'))
sql_uri = 'mysql+pymysql://root:Vickeyiscool@vickey@127.0.0.1:3306/VickeyBlog'


class Config(object):
    SQLALCHEMY_DATABASE_URI = sql_uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False