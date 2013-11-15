#coding:utf-8
from scapp.extensions import db
import json

# 用户、角色 关联表
class SC_UserRole(db.Model):
    __tablename__ = 'sc_userrole' 
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('sc_user.id'))
    role_id = db.Column(db.Integer, db.ForeignKey('sc_role.id'))
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)


# 用户表
class SC_User(db.Model):
    __tablename__ = 'sc_user' 
    id = db.Column(db.Integer, primary_key=True)
    login_name = db.Column(db.String(16))
    login_password = db.Column(db.String(16))
    real_name = db.Column(db.String(32))
    sex = db.Column(db.String(1))
    mobile = db.Column(db.String(16))
    department = db.Column(db.Integer)
    is_active = db.Column(db.String(1))
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)
    # 多对多关系
    userrole = db.relationship('SC_Role', secondary="sc_userrole",backref=db.backref('users', lazy='dynamic'))

# 角色表
class SC_Role(db.Model):
    __tablename__ = 'sc_role' 
    id = db.Column(db.Integer, primary_key=True)
    role_name = db.Column(db.String(16))
    role_level = db.Column(db.Integer)
    # privileges = db.relationship('SC_Privilege', backref='role',lazy='dynamic')

    def __init__(self, role_name, role_level):
        self.role_name = role_name
        self.role_level = role_level

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 权限表
class SC_Privilege(db.Model):
    __tablename__ = 'sc_privilege' 
    id = db.Column(db.Integer, primary_key=True)
    privilege_master = db.Column(db.String(8))
    priviliege_master_id = db.Column(db.Integer, db.ForeignKey('sc_role.id'))
    priviliege_access = db.Column(db.String(16))
    priviliege_access_value = db.Column(db.Integer)
    priviliege_operation = db.Column(db.String(32))
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

    def __init__(self, priviliege_master_id, priviliege_access,priviliege_operation):
        self.priviliege_master_id = priviliege_master_id
        self.priviliege_access = priviliege_access
        self.priviliege_operation = priviliege_operation

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

# 菜单表
class SC_Menu(db.Model):
    __tablename__ = 'sc_menu' 
    id = db.Column(db.Integer, primary_key=True)
    menu_name = db.Column(db.String(32))
    menu_parent = db.Column(db.Integer)
    url = db.Column(db.String(32))
    application = db.Column(db.String(32))
    menu_icon = db.Column(db.String(128))
    is_visible = db.Column(db.Integer)
    is_leaf = db.Column(db.Integer)
    create_user = db.Column(db.Integer)
    create_date = db.Column(db.DateTime)
    modify_user = db.Column(db.Integer)
    modify_date = db.Column(db.DateTime)

# 支行表
class SC_Org(db.Model):
    __tablename__ = 'sc_org' 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32))
    pId = db.Column(db.Integer)
    open = db.Column(db.Boolean)

    def __init__(self, name, pId):
        self.name = name
        self.pId = pId
        self.open = True

    def add(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()