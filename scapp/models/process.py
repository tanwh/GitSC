#coding:utf-8
from flask import Module, session, request, render_template, redirect, url_for
from scapp.extensions import db
import datetime

# 用户表
class SC_Customer_Register(db.Model):
    __tablename__ = 'SC_Customer_Register' 
    id = db.Column(db.Integer, primary_key=True)
    manager=db.Column(db.Integer, db.ForeignKey('sc_user.id'))
    customer_name = db.Column(db.String(16)) #客户名称
    sex = db.Column(db.String(1)) #性别
    age = db.Column(db.String(16)) #年龄
    address = db.Column(db.String(128)) #地址
    industry = db.Column(db.Integer, db.ForeignKey('sc_industry.id')) #所属行业
    business_content = db.Column(db.String(256)) #经营内容
    period = db.Column(db.String(16)) #经营期限
    mobile = db.Column(db.String(16)) #电话
    loan_purpose = db.Column(db.String(256)) #贷款目的
    loan_amount = db.Column(db.String(16)) #贷款数额
    info_source = db.Column(db.Integer, db.ForeignKey('sc_info_source.id')) #信息途径
    remarks = db.Column(db.String(256)) #备注
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    # 外键名称
    user_for_cr = db.relationship('SC_User', backref = db.backref('user_for_cr', lazy = 'dynamic'))
    # 外键名称
    industry_type_name_for_cr = db.relationship('SC_Industry', backref = db.backref('industry_type_name_for_cr', lazy = 'dynamic'))
    # 外键名称
    info_source_name = db.relationship('SC_Info_Source', backref = db.backref('info_source_name', lazy = 'dynamic'))

    def __init__(self,manager,customer_name,sex,age,
                address,industry,business_content,period,mobile,
                loan_purpose,loan_amount,info_source,remarks):
        self.manager = manager
        self.customer_name = customer_name
        self.sex = sex
        self.age = age
        self.address = address
        self.industry = industry
        self.business_content = business_content
        self.period = period
        self.mobile = mobile
        self.loan_purpose = loan_purpose
        self.loan_amount = loan_amount
        self.info_source = info_source
        self.remarks = remarks
        self.create_user = session['login_id']
        self.create_date = datetime.datetime.now()
        self.modify_user = session['login_id']
        self.modify_date = datetime.datetime.now()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()