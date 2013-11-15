# coding:utf-8
from scapp.extensions import db
from flask import Module, session, request, render_template, redirect, url_for

from scapp.models.information import SC_Credentials_Type
from scapp.models.information import SC_Living_Conditions
from scapp.models.information import SC_Education
from scapp.models.information import SC_Relation_Type
from scapp.models.information import SC_Industry
from scapp.models.information import SC_Regisiter_Type
from scapp.models.information import SC_Business_Type
from scapp.models.information import SC_Asset_Type
from scapp.models.information import SC_Info_Source

from scapp.models import SC_Role
from scapp.models import SC_Privilege
from scapp.models import SC_Org

import scapp.helpers as helpers

system = Module(__name__)

# 新增用户
@system.route('/System/new_user', methods=['GET'])
def new_user():
    return render_template("System/new_user.html")

# 新增角色
@system.route('/System/new_role', methods=['GET','POST'])
def new_role():
	if request.method == 'POST':
		# 保存角色
		role = SC_Role(request.form['role_name'], request.form['role_level'])
		role.add()

		# 保存具体权限
		SC_Privilege(role.id,'xxgl',request.form['xxgl']).add()
		SC_Privilege(role.id,'khxxgl',request.form['khxxgl']).add()
		SC_Privilege(role.id,'dkxxgl',request.form['dkxxgl']).add()
		SC_Privilege(role.id,'lcgl',request.form['lcgl']).add()
		SC_Privilege(role.id,'lfdj',request.form['lfdj']).add()
		SC_Privilege(role.id,'dksq',request.form['dksq']).add()
		SC_Privilege(role.id,'dksqsh',request.form['dksqsh']).add()
		SC_Privilege(role.id,'dqdc',request.form['dqdc']).add()
		SC_Privilege(role.id,'dksp',request.form['dksp']).add()
		SC_Privilege(role.id,'dkfk',request.form['dkfk']).add()
		SC_Privilege(role.id,'fksh',request.form['fksh']).add()
		SC_Privilege(role.id,'hkdj',request.form['hkdj']).add()
		SC_Privilege(role.id,'dhbg',request.form['dhbg']).add()
		SC_Privilege(role.id,'dhbgsh',request.form['dhbgsh']).add()
		SC_Privilege(role.id,'dhgl',request.form['dhgl']).add()
		SC_Privilege(role.id,'zcfl',request.form['zcfl']).add()
		SC_Privilege(role.id,'zcflsh',request.form['zcflsh']).add()
		SC_Privilege(role.id,'xtgj',request.form['xtgj']).add()
		SC_Privilege(role.id,'hkjhjsgj',request.form['hkjhjsgj']).add()
		SC_Privilege(role.id,'xtgl',request.form['xtgl']).add()
		SC_Privilege(role.id,'ywcspz',request.form['ywcspz']).add()
		SC_Privilege(role.id,'jkpz',request.form['jkpz']).add()
		SC_Privilege(role.id,'rzrj',request.form['rzrj']).add()
		SC_Privilege(role.id,'sjzd',request.form['sjzd']).add()
		SC_Privilege(role.id,'jggl',request.form['jggl']).add()
		SC_Privilege(role.id,'syzgl',request.form['syzgl']).add()
		SC_Privilege(role.id,'jsqxgl',request.form['jsqxgl']).add()
		SC_Privilege(role.id,'tjbb',request.form['tjbb']).add()
		SC_Privilege(role.id,'kh',request.form['kh']).add()
		SC_Privilege(role.id,'dkgjztfl',request.form['dkgjztfl']).add()
		SC_Privilege(role.id,'xdgzlclb',request.form['xdgzlclb']).add()
		SC_Privilege(role.id,'pcscbbcx',request.form['pcscbbcx']).add()
		SC_Privilege(role.id,'zhgllbb',request.form['zhgllbb']).add()

		return redirect('System/jsqxgl/1')

	elif request.method == 'GET':
		return render_template("System/new_role.html")

# 更新角色
@system.route('/System/edit_role/<int:id>', methods=['GET','POST'])
def edit_role(id):
	if request.method == 'POST':
		# 更新角色(注释掉的用于单条记录更新)
		#role = SC_Role.query.filter_by(id=id).first()
		#role.role_name = request.form['role_name']
		#role.update()
		SC_Role.query.filter_by(id=id).update({"role_name":request.form['role_name'],"role_level":request.form['role_level']})

		# 更新权限
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='xxgl').update({"priviliege_operation":request.form['xxgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='khxxgl').update({"priviliege_operation":request.form['khxxgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dkxxgl').update({"priviliege_operation":request.form['dkxxgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='lcgl').update({"priviliege_operation":request.form['lcgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='lfdj').update({"priviliege_operation":request.form['lfdj']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dksq').update({"priviliege_operation":request.form['dksq']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dksqsh').update({"priviliege_operation":request.form['dksqsh']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dqdc').update({"priviliege_operation":request.form['dqdc']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dksp').update({"priviliege_operation":request.form['dksp']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dkfk').update({"priviliege_operation":request.form['dkfk']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='fksh').update({"priviliege_operation":request.form['fksh']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='hkdj').update({"priviliege_operation":request.form['hkdj']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dhbg').update({"priviliege_operation":request.form['dhbg']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dhbgsh').update({"priviliege_operation":request.form['dhbgsh']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dhgl').update({"priviliege_operation":request.form['dhgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='zcfl').update({"priviliege_operation":request.form['zcfl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='zcflsh').update({"priviliege_operation":request.form['zcflsh']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='xtgj').update({"priviliege_operation":request.form['xtgj']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='hkjhjsgj').update({"priviliege_operation":request.form['hkjhjsgj']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='xtgl').update({"priviliege_operation":request.form['xtgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='ywcspz').update({"priviliege_operation":request.form['ywcspz']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='jkpz').update({"priviliege_operation":request.form['jkpz']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='rzrj').update({"priviliege_operation":request.form['rzrj']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='sjzd').update({"priviliege_operation":request.form['sjzd']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='jggl').update({"priviliege_operation":request.form['jggl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='syzgl').update({"priviliege_operation":request.form['syzgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='jsqxgl').update({"priviliege_operation":request.form['jsqxgl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='tjbb').update({"priviliege_operation":request.form['tjbb']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='kh').update({"priviliege_operation":request.form['kh']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='dkgjztfl').update({"priviliege_operation":request.form['dkgjztfl']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='xdgzlclb').update({"priviliege_operation":request.form['xdgzlclb']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='pcscbbcx').update({"priviliege_operation":request.form['pcscbbcx']})
		SC_Privilege.query.filter_by(priviliege_master_id=id,priviliege_access='zhgllbb').update({"priviliege_operation":request.form['zhgllbb']})

		# 批量提交
		db.session.commit()

		return redirect('System/jsqxgl/1')

	elif request.method == 'GET':
		role = SC_Role.query.filter_by(id=id).first()
		privileges = SC_Privilege.query.filter_by(priviliege_master_id=id).order_by(SC_Privilege.id).all()

		return render_template("System/edit_role.html",role=role,privileges=privileges)

# 新增数据字典
@system.route('/System/new_sjzd/<tablename>', methods=['GET','POST'])
def new_sjzd(tablename):
	if request.method == 'POST':
		eval(tablename+'('+request.form['type_name']+')').add()
		return redirect('System/sjzd')
	else:
		return render_template("System/new_sjzd.html",tablename=tablename)

# 更新数据字典
@system.route('/System/edit_sjzd/<tablename>/<int:id>', methods=['GET','POST'])
def edit_sjzd(tablename,id):
	if request.method == 'POST':
		obj = eval(tablename).query.filter_by(id=id).first()
		obj.type_name = request.form['type_name']
		obj.update()
		return redirect('System/sjzd')
	else:
		obj = eval(tablename).query.filter_by(id=id).first()
		return render_template("System/edit_sjzd.html",tablename=tablename,obj=obj)

# 加载树
@system.route('/System/tree/<tablename>/<int:id>', methods=['GET','POST'])
def init_tree(tablename,id):
	# 加载所有
	if id == 0:
		tree = eval(tablename).query.order_by("id").all()

	# 加载对应id的子节点
	else:
		tree = eval(tablename).query.filter_by(pId=id).order_by("id").all()

	return helpers.show_result_content(tree) # 返回json

# 新增机构
@system.route('/System/new_jggl/<int:pId>', methods=['GET','POST'])
def new_jggl(pId):
	if request.method == 'POST':
		SC_Org(request.form['name'],pId).add()
		return redirect('System/jggl')
	else:
		return render_template("System/new_jggl.html",pId=pId)

# 新增机构
@system.route('/System/edit_jggl/<int:id>', methods=['GET','POST'])
def edit_jggl(id):
	if request.method == 'POST':
		obj = SC_Org.query.filter_by(id=id).first()
		obj.name = request.form['name']
		obj.update()
		return redirect('System/jggl')
	else:
		obj = SC_Org.query.filter_by(id=id).first()
		return render_template("System/edit_jggl.html",obj=obj)