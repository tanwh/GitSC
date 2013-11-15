#coding:utf-8
from flask import session

from scapp.models.system import SC_User

from scapp.extensions import db

import datetime
import json

# 个人客户基本信息表
class SC_Individual_Customer(db.Model):
    __tablename__ = 'sc_individual_customer'
    id=db.Column(db.Integer, primary_key=True)
    customer_no=db.Column(db.String(16))
    customer_type=db.Column(db.String(16))
    customer_name=db.Column(db.String(128))
    manager=db.Column(db.Integer, db.ForeignKey('sc_user.id'))
    credentials_type=db.Column(db.Integer, db.ForeignKey('sc_credentials_type.id'))
    credentials_no=db.Column(db.String(32))
    credentials_org=db.Column(db.String(64))
    credentials_valid=db.Column(db.DateTime)
    sex=db.Column(db.String(1))
    birthday=db.Column(db.DateTime)
    marriage=db.Column(db.String(1))
    family=db.Column(db.String(256))
    living_conditions=db.Column(db.Integer, db.ForeignKey('sc_living_conditions.id'))
    position=db.Column(db.String(32))
    company=db.Column(db.String(64))
    residence_address=db.Column(db.String(128))
    current_address=db.Column(db.String(128))
    work_address=db.Column(db.String(128))
    other_address=db.Column(db.String(128))
    education=db.Column(db.Integer, db.ForeignKey('sc_education.id'))
    telephone=db.Column(db.String(16))
    mobile=db.Column(db.String(16))
    contact_phone=db.Column(db.String(16))
    email=db.Column(db.String(32))
    is_active = db.Column(db.String(1))
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    # 外键名称
    user_for_individual = db.relationship('SC_User', backref = db.backref('user_for_individual', lazy = 'dynamic'))

    def __init__(self, customer_no,customer_name,manager,credentials_type,credentials_no,
                credentials_org,credentials_valid,sex,birthday,marriage,family,living_conditions,position,
                company,residence_address,current_address,work_address,other_address,education,telephone,
                mobile,contact_phone,email,is_active):
        self.customer_no = customer_no
        self.customer_type = 'Individual'
        self.customer_name = customer_name
        self.manager = manager
        self.credentials_type = credentials_type
        self.credentials_no = credentials_no
        self.credentials_org = credentials_org
        self.credentials_valid = credentials_valid
        self.sex = sex
        self.birthday = birthday
        self.marriage = marriage
        self.family = family
        self.living_conditions = living_conditions
        self.position = position
        self.company = company
        self.residence_address = residence_address
        self.current_address = current_address
        self.work_address = work_address
        self.other_address = other_address
        self.education = education
        self.telephone = telephone
        self.mobile = mobile
        self.contact_phone = contact_phone
        self.email = email
        self.is_active = is_active
        self.create_user = session['login_id']
        self.create_date = datetime.datetime.now()
        self.modify_user = session['login_id']
        self.modify_date = datetime.datetime.now()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 业务往来表
class SC_Dealings(db.Model):
    __tablename__ = 'sc_dealings'
    id=db.Column(db.Integer, primary_key=True)
    deal_name=db.Column(db.String(32))
    deal_description=db.Column(db.String(128))
    belong_customer_type=db.Column(db.String(16))
    belong_customer_value=db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    def __init__(self, deal_name, deal_description, belong_customer_type, belong_customer_value):
        self.deal_name = deal_name
        self.deal_description = deal_description
        self.belong_customer_type = belong_customer_type
        self.belong_customer_value = belong_customer_value

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 证件类型表
class SC_Credentials_Type(db.Model):
    __tablename__ = 'sc_credentials_type'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 居住条件表
class SC_Living_Conditions(db.Model):
    __tablename__ = 'sc_living_conditions'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 教育程度表
class SC_Education(db.Model):
    __tablename__ = 'sc_education'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 公司客户基本表
class SC_Company_Customer(db.Model):
    __tablename__ = 'sc_company_customer'
    id=db.Column(db.Integer, primary_key=True)
    manager=db.Column(db.Integer, db.ForeignKey('sc_user.id'))
    customer_no=db.Column(db.String(16))
    company_name=db.Column(db.String(128))
    customer_type=db.Column(db.String(16))
    frdb=db.Column(db.String(32))
    yyzz=db.Column(db.String(32))
    yyzz_fzjg=db.Column(db.String(64))
    swdjz=db.Column(db.String(32))
    swdjz_fzjg=db.Column(db.String(64))
    gszczj=db.Column(db.Integer, db.ForeignKey('sc_regisiter_type.id'))
    gsyyfw=db.Column(db.String(128))
    gsclrq=db.Column(db.DateTime)
    gszclx=db.Column(db.Integer)
    jbhzh=db.Column(db.String(32))
    zcdz=db.Column(db.String(128))
    xdz=db.Column(db.String(128))
    bgdz=db.Column(db.String(128))
    qtdz=db.Column(db.String(128))
    education=db.Column(db.Integer, db.ForeignKey('sc_education.id'))
    family=db.Column(db.String(256))
    telephone=db.Column(db.String(16))
    mobile=db.Column(db.String(16))
    contact_phone=db.Column(db.String(16))
    email=db.Column(db.String(32))
    is_active=db.Column(db.String(1))
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    # 外键名称
    user_for_company = db.relationship('SC_User', backref = db.backref('user_for_company', lazy = 'dynamic'))
    
    def __init__(self, manager,customer_no,company_name,frdb,yyzz,yyzz_fzjg,swdjz,swdjz_fzjg,
                gszczj,gsyyfw,gsclrq,gszclx,jbhzh,zcdz,xdz,bgdz,
                qtdz,education,family,telephone,mobile,contact_phone,email):
        self.manager = manager
        self.customer_no = customer_no
        self.customer_type = 'Company'
        self.company_name = company_name
        self.frdb = frdb
        self.yyzz = yyzz
        self.yyzz_fzjg = yyzz_fzjg
        self.swdjz = swdjz
        self.swdjz_fzjg = swdjz_fzjg
        self.gszczj = gszczj
        self.gsyyfw = gsyyfw
        self.gsclrq = gsclrq
        self.gszclx = gszclx
        self.jbhzh = jbhzh
        self.zcdz = zcdz
        self.xdz = xdz
        self.bgdz = bgdz
        self.qtdz = qtdz
        self.education = education
        self.family = family
        self.telephone = telephone
        self.mobile = mobile
        self.contact_phone = contact_phone
        self.email = email
        self.create_user = session['login_id']
        self.create_date = datetime.datetime.now()
        self.modify_user = session['login_id']
        self.modify_date = datetime.datetime.now()

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 关系人信息表
class SC_Relations(db.Model):
    __tablename__ = 'sc_relations'
    id=db.Column(db.Integer, primary_key=True)
    relation_no=db.Column(db.String(16))
    relation_name=db.Column(db.String(32))
    relation_type=db.Column(db.Integer, db.ForeignKey('sc_relation_type.id'))
    cgbl=db.Column(db.Float)
    business_name=db.Column(db.String(128))
    relation_describe=db.Column(db.String(128))
    belong_customer_type=db.Column(db.String(16))
    belong_customer_value=db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    # 外键名称
    relation_type_name = db.relationship('SC_Relation_Type', backref = db.backref('relation_type_name', lazy = 'dynamic'))

    def __init__(self, relation_no, relation_name, relation_type, cgbl, business_name, relation_describe,
        belong_customer_type, belong_customer_value):
        self.relation_no = relation_no
        self.relation_name = relation_name
        self.relation_type = relation_type
        self.cgbl = cgbl
        self.business_name = business_name
        self.relation_describe = relation_describe
        self.belong_customer_type = belong_customer_type
        self.belong_customer_value = belong_customer_value

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 关系类型表
class SC_Relation_Type(db.Model):
    __tablename__ = 'sc_relation_type'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 经营信息表
class SC_Manage_Info(db.Model):
    __tablename__ = 'sc_manage_info'
    id=db.Column(db.Integer, primary_key=True)
    business_name=db.Column(db.String(32))
    industry=db.Column(db.Integer, db.ForeignKey('sc_industry.id'))
    business_description=db.Column(db.String(128))
    business_type=db.Column(db.Integer, db.ForeignKey('sc_business_type.id'))
    stake=db.Column(db.String(4))
    business_address=db.Column(db.String(128))
    annual_income=db.Column(db.Integer)
    monthly_income=db.Column(db.Integer)
    establish_date=db.Column(db.DateTime)
    employees=db.Column(db.Integer)
    manager_name=db.Column(db.Integer)
    credentials_type=db.Column(db.Integer, db.ForeignKey('sc_credentials_type.id'))
    credentials_no=db.Column(db.String(32))
    credentials_org=db.Column(db.String(64))
    belong_customer_type=db.Column(db.String(16))
    belong_customer_value=db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    # 外键名称
    industry_type_name = db.relationship('SC_Industry', backref = db.backref('industry_type_name', lazy = 'dynamic'))
    # 外键名称
    business_type_name = db.relationship('SC_Business_Type', backref = db.backref('business_type_name', lazy = 'dynamic'))
    # 外键名称
    credentials_type_name = db.relationship('SC_Credentials_Type', backref = db.backref('credentials_type_name', lazy = 'dynamic'))

    def __init__(self, business_name, industry, business_description, business_type,
        stake, business_address, annual_income, monthly_income,
        establish_date, employees, manager_name, credentials_type,
        credentials_no, credentials_org,belong_customer_type,belong_customer_value):
        self.business_name = business_name
        self.industry = industry
        self.business_description = business_description
        self.business_type = business_type
        self.stake = stake
        self.business_address = business_address
        self.annual_income = annual_income
        self.monthly_income = monthly_income
        self.establish_date = establish_date
        self.employees = employees
        self.manager_name = manager_name
        self.credentials_type = credentials_type
        self.credentials_no = credentials_no
        self.credentials_org = credentials_org
        self.belong_customer_type = belong_customer_type
        self.belong_customer_value = belong_customer_value

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 所属行业表
class SC_Industry(db.Model):
    __tablename__ = 'sc_industry'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(32))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 资产信息表
class SC_Asset_Info(db.Model):
    __tablename__ = 'sc_asset_info'
    id=db.Column(db.Integer, primary_key=True)
    asset_name=db.Column(db.String(32))
    asset_type=db.Column(db.Integer, db.ForeignKey('sc_asset_type.id'))
    asset_description=db.Column(db.String(128))
    asset_position=db.Column(db.String(128))
    credentials_name=db.Column(db.String(32))
    credentials_no=db.Column(db.String(64))
    appraisal=db.Column(db.DECIMAL(18,2))
    is_mortgage=db.Column(db.String(1))
    mortgage_amount=db.Column(db.DECIMAL(18,2))
    mortgage_object=db.Column(db.String(32))
    belong_customer_type=db.Column(db.String(16))
    belong_customer_value=db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    # 外键名称
    asset_type_name = db.relationship('SC_Asset_Type', backref = db.backref('asset_type_name', lazy = 'dynamic'))

    def __init__(self, asset_name, asset_type, asset_description, asset_position,
        credentials_name,credentials_no, appraisal, is_mortgage, mortgage_amount,
        mortgage_object,belong_customer_type,belong_customer_value):
        self.asset_name = asset_name
        self.asset_type = asset_type
        self.asset_description = asset_description
        self.asset_position = asset_position
        self.credentials_name = credentials_name
        self.credentials_no = credentials_no
        self.appraisal = appraisal
        self.is_mortgage = is_mortgage
        self.mortgage_amount = mortgage_amount
        self.mortgage_object = mortgage_object
        self.belong_customer_type = belong_customer_type
        self.belong_customer_value = belong_customer_value

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 财务信息表
class SC_Financial_Affairs(db.Model):
    __tablename__ = 'sc_financial_affairs'
    id=db.Column(db.Integer, primary_key=True)
    main_supplier=db.Column(db.String(128))
    main_client=db.Column(db.String(128))
    total_assets=db.Column(db.String(128))
    stock=db.Column(db.String(128))
    accounts=db.Column(db.String(128))
    fixed_assets=db.Column(db.String(128))
    total_liabilities=db.Column(db.String(128))
    bank_borrowings=db.Column(db.String(128))
    private_borrowers=db.Column(db.String(128))
    monthly_sales=db.Column(db.String(128))
    profit=db.Column(db.String(128))
    other_monthly_income=db.Column(db.String(128))
    belong_customer_type=db.Column(db.String(16))
    belong_customer_value=db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    def __init__(self,
        main_supplier, main_client, total_assets,
        stock, accounts,fixed_assets,
        total_liabilities, bank_borrowings,private_borrowers,
        monthly_sales, profit, other_monthly_income,
        belong_customer_type,belong_customer_value,):
        self.main_supplier = main_supplier
        self.main_client = main_client
        self.total_assets = total_assets
        self.stock = stock
        self.accounts = accounts
        self.fixed_assets = fixed_assets
        self.total_liabilities = total_liabilities
        self.bank_borrowings = bank_borrowings
        self.private_borrowers = private_borrowers
        self.monthly_sales = monthly_sales
        self.profit = profit
        self.other_monthly_income = other_monthly_income
        self.belong_customer_type = belong_customer_type
        self.belong_customer_value = belong_customer_value

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 其他信息表
class SC_Other_Info(db.Model):
    __tablename__ = 'sc_other_info'
    id=db.Column(db.Integer, primary_key=True)
    info_name=db.Column(db.String(32))
    info_description=db.Column(db.String(128))
    attachment=db.Column(db.String(128))
    belong_customer_type=db.Column(db.String(16))
    belong_customer_value=db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    def __init__(self, info_name, info_description, attachment,
        belong_customer_type,belong_customer_value):
        self.info_name = info_name
        self.info_description = info_description
        self.attachment = attachment
        self.belong_customer_type = belong_customer_type
        self.belong_customer_value = belong_customer_value

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 注册类型表
class SC_Regisiter_Type(db.Model):
    __tablename__ = 'sc_regisiter_type'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 经营性质表
class SC_Business_Type(db.Model):
    __tablename__ = 'sc_business_type'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 资产类型表
class SC_Asset_Type(db.Model):
    __tablename__ = 'sc_asset_type'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name
        
    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 信息途径表
class SC_Info_Source(db.Model):
    __tablename__ = 'sc_info_source'
    id=db.Column(db.Integer, primary_key=True)
    type_name=db.Column(db.String(16))

    def __init__(self, type_name):
        self.type_name = type_name
        
    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()