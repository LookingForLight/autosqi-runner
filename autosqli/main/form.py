# -*-coding:utf-8-*-
from flask_wtf import FlaskForm
from wtforms import validators, fields, widgets
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, UniqueConstraint, Index,DateTime
from datetime import datetime
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
from utils.mod_db import sqlalchemy_op
Base = declarative_base()
class TaskInfo(Base):
    __tablename__ = 'taskinfo'
    id = Column(Integer,primary_key=True,autoincrement=True)
    taskid = Column(String(45))
    status = Column(String(45))
    createtime=Column(DateTime(),default=datetime.now)

def init_db():
    sql_db = sqlalchemy_op()
    Base.metadata.create_all(sql_db._engine)
class MyForm(FlaskForm):
    Username = fields.StringField(
        label='用户名1',
        validators=[
            validators.DataRequired(message='用户名不能为空'),
            validators.length(min=6, max=11, message='用户名长度必须大于%(min)d且小于%(max)d')
        ],
        widget=widgets.TextInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入用户名1',
            'required': '',
            'autofocus': ''
        }
    )
    Password = fields.PasswordField(
        label='密码',
        validators=[
            validators.DataRequired(message='密码不能为空'),
            validators.length(min=6, message='密码必须大于%(min)d位')
        ],
        widget=widgets.PasswordInput(),
        render_kw={
            'class': 'form-control',
            'placeholder': '请输入密码',
            'required': '',
            'autofocus': ''
        }
    )


class AutosqliForm(FlaskForm):
    test_url = fields.StringField(

        label="TEST URL:",
        validators=[
            validators.DataRequired(message='URL不能为空'),
            validators.URL(require_tld=False, message='url不正确')
        ],
        widget = widgets.TextInput(),
        render_kw={
            "class": "form-control",
            "placeholder": "请输入URL",
            "required": "",
            "autofocus": ""
        }
    )

    request_method = fields.RadioField(

        label="请求方法",
        validators=[
            validators.DataRequired(message='请选择请求方法'),
        ],
        choices=[('get', "GET"),('post','POST')],
        default='post'
    )

    request_params = fields.TextAreaField(
        label='请求参数',
        validators=[
            validators.DataRequired(message='请求参数不能为空')

        ],
        widget=widgets.TextArea(),
        render_kw={
            'class':'form-control',
            'required':'',
            'rows':6
        }
    )

    ignore_params = fields.StringField(
        label='忽略注入字段',
        widget=widgets.TextInput(),
        render_kw={
                'class':'form-control',
                'placeholder':'输入不要检测的字段名'
        }
    )
