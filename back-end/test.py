from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URL'] = 'mysql+pymysql://root:Vickeyiscool@vickey@127.0.0.1:3306/BlogBase'
app.config['']