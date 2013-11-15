# coding:utf-8

from flask import Module, session, request, render_template, redirect, url_for

from scapp.config import PER_PAGE

from scapp.models import SC_User

from scapp.models import SC_Industry
from scapp.models import SC_Info_Source
from scapp.models import SC_Customer_Register

process = Module(__name__)

# 来访登记
@process.route('/Process/lfdj/lfdj_search/<int:page>', methods=['POST'])
def lfdj_search(page):
    customer_register = SC_Customer_Register.query.order_by("id").paginate(page, per_page = PER_PAGE)
    return render_template("Process/lfdj/lfdj.html",customer_register=customer_register)

# 新增来访登记
@process.route('/Process/lfdj/new_lfdj', methods=['GET','POST'])
def new_lfdj():
    if request.method == 'POST' :
        SC_Customer_Register(request.form['manager'],request.form['customer_name'],request.form['sex'],
            request.form['age'],request.form['address'],request.form['industry'],request.form['business_content'],
            request.form['period'],request.form['mobile'],request.form['loan_purpose'],request.form['loan_amount'],
            request.form['info_source'],request.form['remarks']).add()
        return redirect('Process/lfdj/lfdj')
    else :
        user = SC_User.query.order_by("id").all()
        industry = SC_Industry.query.order_by("id").all()
        info_source = SC_Info_Source.query.order_by("id").all()
        return render_template("Process/lfdj/new_lfdj.html",user=user,industry=industry,info_source=info_source)

# 编辑来访登记
@process.route('/Process/lfdj/edit_lfdj/<int:id>', methods=['GET','POST'])
def edit_lfdj(id):
    if request.method == 'POST' :
        customer_register = SC_Customer_Register.query.filter_by(id=id).first()

        customer_register.manager = request.form['manager']
        customer_register.customer_name = request.form['customer_name']
        customer_register.sex = request.form['sex']
        customer_register.age = request.form['age']
        customer_register.address = request.form['address']
        customer_register.industry = request.form['industry']
        customer_register.business_content = request.form['business_content']
        customer_register.period = request.form['period']
        customer_register.mobile = request.form['mobile']
        customer_register.loan_purpose = request.form['loan_purpose']
        customer_register.loan_amount = request.form['loan_amount']
        customer_register.info_source = request.form['info_source']
        customer_register.remarks = request.form['remarks']

        customer_register.update()

        return redirect('Process/lfdj/lfdj')
    else :
        customer_register = SC_Customer_Register.query.filter_by(id=id).first()
        user = SC_User.query.order_by("id").all()
        industry = SC_Industry.query.order_by("id").all()
        info_source = SC_Info_Source.query.order_by("id").all()
        return render_template("Process/lfdj/edit_lfdj.html",customer_register=customer_register,
            user=user,industry=industry,info_source=info_source)

# 贷款申请
@process.route('/Process/dksq/dksq_search/<int:page>', methods=['POST'])
def dksq_search(page):
    return render_template("Process/dksq/dksq.html")

# 新增贷款申请
@process.route('/Process/dksq/new_dksq', methods=['GET'])
def new_dksq():
    return render_template("Process/dksq/new_dksq.html")

# 编辑贷款申请信息
@process.route('/Process/dksq/edit_dksq', methods=['GET'])
def edit_dksq():
    return render_template("Process/dksq/edit_dksq.html")

# 贷款申请信息
@process.route('/Process/dksq/dksq_info', methods=['GET'])
def dksq_info():
    return render_template("Process/dksq/dksq_info.html")

# 编辑贷款申请审核信息
@process.route('/Process/dksqsh/edit_dksqsh', methods=['GET'])
def edit_dksqsh():
    return render_template("Process/dksqsh/edit_dksqsh.html")

# 贷款申请审核信息
@process.route('/Process/dksqsh/dksqsh_info', methods=['GET'])
def dksqsh_info():
    return render_template("Process/dksqsh/dksqsh_info.html")

# 贷款调查——微贷
@process.route('/Process/dqdc/dqdc_wd', methods=['GET'])
def dqdc_wd():
    return render_template("Process/dqdc/dqdc_wd.html")

# 贷款调查——微贷信息
@process.route('/Process/dqdc/dqdc_wd_info', methods=['GET'])
def dqdc_wd_info():
    return render_template("Process/dqdc/dqdc_wd_info.html")

# 贷款调查——微贷(基本情况)
@process.route('/Process/dqdc/dqdcWd_jbqk', methods=['GET'])
def dqdcWd_jbqk():
    return render_template("Process/dqdc/dqdcWd_jbqk.html")

# 贷款调查——微贷(资产负债表)
@process.route('/Process/dqdc/dqdcWd_zcfzb', methods=['GET'])
def dqdcWd_zcfzb():
    return render_template("Process/dqdc/dqdcWd_zcfzb.html")

# 贷款调查——微贷(益损表)
@process.route('/Process/dqdc/dqdcWd_syb', methods=['GET'])
def dqdcWd_syb():
    return render_template("Process/dqdc/dqdcWd_syb.html")

# 贷款调查——小额贷款
@process.route('/Process/dqdc/dqdc_xed', methods=['GET'])
def dqdc_xed():
    return render_template("Process/dqdc/dqdc_xed.html")

# 贷款调查——小额贷款(基本情况)
@process.route('/Process/dqdc/dqdcXed_jbqk', methods=['GET'])
def dqdcXed_jbqk():
    return render_template("Process/dqdc/dqdcXed_jbqk.html")
    
# 贷款调查——小额贷款(资产负债表)
@process.route('/Process/dqdc/dqdcXed_zcfzb', methods=['GET'])
def dqdcXed_zcfzb():
    return render_template("Process/dqdc/dqdcXed_zcfzb.html")

# 贷款调查——小额贷款(交叉检验)
@process.route('/Process/dqdc/dqdcXed_jcjy', methods=['GET'])
def dqdcXed_jcjy():
    return render_template("Process/dqdc/dqdcXed_jcjy.html")
    
# 贷款调查——小额贷款(损益情况分析)
@process.route('/Process/dqdc/dqdcXed_ysqkfx', methods=['GET'])
def dqdcXed_ysqkfx():
    return render_template("Process/dqdc/dqdcXed_ysqkfx.html")

# 贷款调查——小额贷款(现金流分析)
@process.route('/Process/dqdc/dqdcXed_xjlfx', methods=['GET'])
def dqdcXed_xjlfx():
    return render_template("Process/dqdc/dqdcXed_xjlfx.html")

# 贷款调查——小额贷款(担保抵押调查表)
@process.route('/Process/dqdc/dqdcXed_dbdydcb', methods=['GET'])
def dqdcXed_dbdydcb():
    return render_template("Process/dqdc/dqdcXed_dbdydcb.html")

# 贷款调查——小额贷款(固定资产清单)
@process.route('/Process/dqdc/dqdcXed_gdzcqd', methods=['GET'])
def dqdcXed_gdzcqd():
    return render_template("Process/dqdc/dqdcXed_gdzcqd.html")

# # 贷款调查——小额贷款(固定资产清单——新建房地产)
# @process.route('/Process/dqdc/new_fdc', methods=['GET'])
# def new_fdc():
#     return render_template("Process/dqdc/new_fdc.html")

# 贷款调查——小额贷款(库存)
@process.route('/Process/dqdc/dqdcXed_kc', methods=['GET'])
def dqdcXed_kc():
    return render_template("Process/dqdc/dqdcXed_kc.html")

# 贷款调查——小额贷款(账款清单)
@process.route('/Process/dqdc/dqdcXed_zkqd', methods=['GET'])
def dqdcXed_zkqd():
    return render_template("Process/dqdc/dqdcXed_zkqd.html")

 
# 贷款审批——贷款审批信息(编辑贷款审批)
@process.route('/Process/dksp/edit_dksp', methods=['GET'])
def edit_dksp():
    return render_template("Process/dksp/edit_dksp.html") 

# 贷款审批——贷款审批信息(贷款审议审批表)
@process.route('/Process/dksp/dksp_info', methods=['GET'])
def dksp_info():
    return render_template("Process/dksp/dksp_info.html")


# 贷款放款——编辑放款
@process.route('/Process/dkfk/edit_dkfk', methods=['GET'])
def edit_dkfk():
    return render_template("Process/dkfk/edit_dkfk.html")   

# 贷款放款——编辑放款(放款信息)
@process.route('/Process/dkfk/fkxx', methods=['GET'])
def dkfk_fkxx():
    return render_template("Process/dkfk/fkxx.html")

# 贷款放款——编辑放款(还款计划)
@process.route('/Process/dkfk/hkjh', methods=['GET'])
def dkfk_hkjh():
    return render_template("Process/dkfk/hkjh.html")


# 贷款放款——编辑放款审核
@process.route('/Process/fksh/edit_fksh', methods=['GET'])
def edit_fksh():
    return render_template("Process/fksh/edit_fksh.html")

# 贷款放款——编辑还款登记
@process.route('/Process/hkdj/edit_hkdj', methods=['GET'])
def edit_hkdj():
    return render_template("Process/hkdj/edit_hkdj.html")


# 贷后变更——编辑贷后变更
@process.route('/Process/dhbg/edit_dhbg', methods=['GET'])
def edit_dhbg():
    return render_template("Process/dhbg/edit_dhbg.html")

# 贷后变更——编辑贷后变更(基础信息)
@process.route('/Process/dhbg/jcxx', methods=['GET'])
def dhbg_jcxx():
    return render_template("Process/dhbg/jcxx.html")

# 贷后变更——编辑贷后变更(修改还款计划)
@process.route('/Process/dhbg/edit_hkjh', methods=['GET'])
def edit_hkjh():
    return render_template("Process/dhbg/edit_hkjh.html")

# 贷后变更——编辑贷后变更(修改担保人数据)
@process.route('/Process/dhbg/edit_dbrsj', methods=['GET'])
def edit_dbrsj():
    return render_template("Process/dhbg/edit_dbrsj.html")

# 贷后变更——编辑贷后变更(修改共同借款人数据)
@process.route('/Process/dhbg/edit_gtjkrsj', methods=['GET'])
def edit_gtjkrsj():
    return render_template("Process/dhbg/edit_gtjkrsj.html")

# 贷后变更——编辑贷后变更(修改抵质押物数据)
@process.route('/Process/dhbg/edit_dzywsj', methods=['GET'])
def edit_dzywsj():
    return render_template("Process/dhbg/edit_dzywsj.html")





# 贷后变更审核——审核还款计划
@process.route('/Process/dhbgsh/check_hkjh', methods=['GET'])
def check_hkjh():
    return render_template("Process/dhbgsh/check_hkjh.html")

# 贷后变更审核——审核担保人数据
@process.route('/Process/dhbgsh/check_dbrsj', methods=['GET'])
def check_dbrsj():
    return render_template("Process/dhbgsh/check_dbrsj.html")

# 贷后变更审核——审核共同借款人数据
@process.route('/Process/dhbgsh/check_gtjkrsj', methods=['GET'])
def check_gtjkrsj():
    return render_template("Process/dhbgsh/check_gtjkrsj.html")

# 贷后变更审核——审核抵质押物数据
@process.route('/Process/dhbgsh/check_dzywsj', methods=['GET'])
def check_dzywsj():
    return render_template("Process/dhbgsh/check_dzywsj.html")



# 贷后管理——贷后管理
@process.route('/Process/dhgl/edit_dhgl', methods=['GET'])
def edit_dhgl():
    return render_template("Process/dhgl/edit_dhgl.html")

# 贷后管理——新增标准
@process.route('/Process/dhgl/new_bz', methods=['GET'])
def new_bz():
    return render_template("Process/dhgl/new_bz.html")

# 贷后管理——新增非标准
@process.route('/Process/dhgl/new_fbz', methods=['GET'])
def new_fbz():
    return render_template("Process/dhgl/new_fbz.html")
        
# 贷后管理——管理信息列表
@process.route('/Process/dhgl/glxxlb', methods=['GET'])
def dhgl_glxxlb():
    return render_template("Process/dhgl/glxxlb.html")

# 贷后管理——管理信息
@process.route('/Process/dhgl/glxx', methods=['GET'])
def dhgl_glxx():
    return render_template("Process/dhgl/glxx.html")

# 贷后管理——非标监控说明
@process.route('/Process/dhgl/fbjksm', methods=['GET'])
def dhgl_fbjksm():
    return render_template("Process/dhgl/fbjksm.html")


# 资产分类——编辑资产分类
@process.route('/Process/zcfl/edit_zcfl', methods=['GET'])
def edit_zcfl():
    return render_template("Process/zcfl/edit_zcfl.html")

# 资产分类审核——审核资产分类
@process.route('/Process/zcflsh/check_zcfl', methods=['GET'])
def check_zcfl():
    return render_template("Process/zcflsh/check_zcfl.html")