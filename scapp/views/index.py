# coding:utf-8

from flask import Module, session, request, render_template, redirect, url_for

from scapp.config import PER_PAGE

from scapp.models import SC_User
from scapp.models import SC_Privilege
from scapp.models import SC_Role
from scapp.models import SC_Org

from scapp.models import SC_Credentials_Type
from scapp.models import SC_Living_Conditions
from scapp.models import SC_Education
from scapp.models import SC_Relation_Type
from scapp.models import SC_Industry
from scapp.models import SC_Regisiter_Type
from scapp.models import SC_Business_Type
from scapp.models import SC_Asset_Type
from scapp.models import SC_Info_Source

import scapp.helpers as helpers

index = Module(__name__)

# 登陆
@index.route('/')
@index.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = SC_User.query.filter_by(login_name=request.form['login_name'], login_password=request.form['login_password']).first()

        # if user:
            # privileges = SC_Privilege.query.filter_by(priviliege_master_id = user.userrole[0].id).all()

        # 移动终端 用隐藏域is_pad做标记 返回不同的结果
        # if request.form.has_key('is_pad') and request.form['is_pad']== '1':
        #     if user:
        #         return helpers.show_result_content(user)
        #     else:
        #         return helpers.show_result_fail()
        # # pc端
        # else:
        if user:
            session['logged_in'] = True
            session['login_id'] = user.id
            session['login_name'] = user.login_name
            #session['privileges'] = privileges
            return render_template("welcome.html",login_name = user.login_name)
        else:
            return render_template("login.html")

    else:
        return render_template("login.html")

# 注销
@index.route('/logout')
def logout():
    # session.pop('logged_in', None)
    # session.pop('login_id', None)
    # session.pop('login_name', None)
    session.clear()
    return render_template("login.html")
    
# 欢迎界面
@index.route('/welcome', methods=['GET'])
def welcome():
    return render_template("welcome.html",login_name = session['login_name'])

# 信息管理
@index.route('/xxgl', methods=['GET'])
def xxgl():
    return render_template("index.html",menu = 'xxgl',login_name = session['login_name'])

# 流程管理
@index.route('/lcgl', methods=['GET'])
def lcgl():
    return render_template("index.html",menu = 'lcgl',login_name = session['login_name'])

# 系统工具
@index.route('/xtgj', methods=['GET'])
def xtgj():
    return render_template("index.html",menu = 'xtgj',login_name = session['login_name'])

# 系统管理
@index.route('/xtgl', methods=['GET'])
def xtgl():
    return render_template("index.html",menu = 'xtgl',login_name = session['login_name'])

# 统计报表
@index.route('/tjbb', methods=['GET'])
def tjbb():
    return render_template("index.html",menu = 'tjbb',login_name = session['login_name'])

# 修改密码
@index.route('/change_password', methods=['GET'])
def change_password():
    return render_template("change_password.html",login_name = session['login_name'])

# 客户信息管理
@index.route('/Information/khxxgl', methods=['GET'])
def Information_khxxgl():
    org = SC_Org.query.order_by("id").all()
    return render_template("Information/khxxgl_search.html",org=org)

# 贷款信息管理
@index.route('/Information/dkxxgl', methods=['GET'])
def Information_dkxxgl():
    return render_template("Information/dkxxgl.html")

# 来访登记
@index.route('/Process/lfdj/lfdj', methods=['GET'])
def Process_lfdj():
    industry = SC_Industry.query.order_by("id").all()
    info_source = SC_Info_Source.query.order_by("id").all()
    return render_template("Process/lfdj/lfdj_search.html",industry=industry,info_source=info_source)

# 贷款申请
@index.route('/Process/dksq/dksq', methods=['GET'])
def Process_dksq():
    return render_template("Process/dksq/dksq_search.html")

# 贷款申请审核
@index.route('/Process/dksqsh/dksqsh', methods=['GET'])
def Process_dksqsh():
    return render_template("Process/dksqsh/dksqsh.html")

# 贷前调查
@index.route('/Process/dqdc/dqdc', methods=['GET'])
def Process_dqdc():
    return render_template("Process/dqdc/dqdc.html")

# 贷款审批
@index.route('/Process/dksp/dksp', methods=['GET'])
def Process_dksp():
    return render_template("Process/dksp/dksp.html")

# 贷款放款
@index.route('/Process/dkfk/dkfk', methods=['GET'])
def Process_dkfk():
    return render_template("Process/dkfk/dkfk.html")

# 房款审核
@index.route('/Process/fksh/fksh', methods=['GET'])
def Process_fksh():
    return render_template("Process/fksh/fksh.html")

# 还款登记
@index.route('/Process/hkdj/hkdj', methods=['GET'])
def Process_hkdj():
    return render_template("Process/hkdj/hkdj.html")

# 贷后变更
@index.route('/Process/dhbg/dhbg', methods=['GET'])
def Process_dhbg():
    return render_template("Process/dhbg/dhbg.html")

# 贷后变更审核
@index.route('/Process/dhbgsh/dhbgsh', methods=['GET'])
def Process_dhbgsh():
    return render_template("Process/dhbgsh/dhbgsh.html")

# 贷后管理
@index.route('/Process/dhgl/dhgl', methods=['GET'])
def Process_dhgl():
    return render_template("Process/dhgl/dhgl.html")

# 资产分类
@index.route('/Process/zcfl/zcfl', methods=['GET'])
def Process_zcfl():
    return render_template("Process/zcfl/zcfl.html")

# 资产分类审核
@index.route('/Process/zcflsh/zcflsh', methods=['GET'])
def Process_zcflsh():
    return render_template("Process/zcflsh/zcflsh.html")

# 还款计划计算工具
@index.route('/Tools/hkjhjsgj', methods=['GET'])
def Tools_hkjhjsgj():
    return render_template("Tools/hkjhjsgj.html")

# 业务参数配置
@index.route('/System/ywcspz', methods=['GET'])
def System_ywcspz():
    return render_template("System/ywcspz.html")

# 接口配置
@index.route('/System/jkpz', methods=['GET'])
def System_jkpz():
    return render_template("System/jkpz.html")

# 日终日结
@index.route('/System/rzrj', methods=['GET'])
def System_rzrj():
    return render_template("System/rzrj.html")

# 数据字典
@index.route('/System/sjzd', methods=['GET'])
def System_sjzd():
    # 获取所有字典
    credentials_type = SC_Credentials_Type.query.order_by("id").all()
    living_conditions = SC_Living_Conditions.query.order_by("id").all()
    education  = SC_Education.query.order_by("id").all()
    relation_Type = SC_Relation_Type.query.order_by("id").all()
    industry = SC_Industry.query.order_by("id").all()
    regisiter_type = SC_Regisiter_Type.query.order_by("id").all()
    business_type = SC_Business_Type.query.order_by("id").all()
    asset_type = SC_Asset_Type.query.order_by("id").all()
    info_source = SC_Info_Source.query.order_by("id").all()

    return render_template("System/sjzd.html", credentials_type=credentials_type, living_conditions=living_conditions
        , education=education, relation_Type=relation_Type, industry=industry
        , regisiter_type=regisiter_type, business_type=business_type, asset_type=asset_type
        , info_source=info_source)

# 机构管理
@index.route('/System/jggl', methods=['GET'])
def System_jggl():
    return render_template("System/jggl.html")
	
# 使用者管理
@index.route('/System/syzgl', methods=['GET'])
def System_syzgl():
    return render_template("System/syzgl.html")

# 角色权限管理
@index.route('/System/jsqxgl/<int:page>', methods=['GET'])
def System_jsqxgl(page):
    # 获取角色并分页
    roles = SC_Role.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("System/jsqxgl.html",roles = roles)

# 客户
@index.route('/Report/kh', methods=['GET'])
def Report_kh():
    return render_template("Report/kh.html")

# 贷款根据状态分类
@index.route('/Report/dkgjztfl', methods=['GET'])
def Report_dkgjztfl():
    return render_template("Report/dkgjztfl.html")

# 信贷工作流程列表
@index.route('/Report/xdgzlclb', methods=['GET'])
def Report_xdgzlclb():
    return render_template("Report/xdgzlclb.html")

# 批次生成报表查询
@index.route('/Report/pcscbbcx', methods=['GET'])
def Report_pcscbbcx():
    return render_template("Report/pcscbbcx.html")

# 总行管理类报表
@index.route('/Report/zhgllbb', methods=['GET'])
def Report_zhgllbb():
    return render_template("Report/zhgllbb.html")

# 折线图
@index.route('/Report/line', methods=['GET'])
def Report_line():
    return render_template("Report/line.html")

# 柱状图
@index.route('/Report/bar', methods=['GET'])
def Report_bar():
    return render_template("Report/bar.html")

# 饼图
@index.route('/Report/pie', methods=['GET'])
def Report_pie():
    return render_template("Report/pie.html")

