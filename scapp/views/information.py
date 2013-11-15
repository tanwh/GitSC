# coding:utf-8

from flask import Module, session, request, render_template, redirect, url_for
from werkzeug import secure_filename
import os

from scapp.config import PER_PAGE
from scapp.config import UPLOAD_FOLDER_REL
from scapp.config import UPLOAD_FOLDER_ABS

from scapp.models import SC_Individual_Customer
from scapp.models import SC_Company_Customer
from scapp.models import SC_Dealings
from scapp.models import SC_Relations
from scapp.models import SC_Manage_Info
from scapp.models import SC_Asset_Info
from scapp.models import SC_Other_Info
from scapp.models import SC_Financial_Affairs
from scapp.models import SC_User

from scapp.models import SC_Credentials_Type
from scapp.models import SC_Living_Conditions
from scapp.models import SC_Education
from scapp.models import SC_Regisiter_Type
from scapp.models import SC_Relation_Type
from scapp.models import SC_Industry
from scapp.models import SC_Business_Type
from scapp.models import SC_Asset_Type

information = Module(__name__)

# 客户信息搜索
@information.route('/Information/khxxgl_search/<int:page>', methods=['POST'])
def khxxgl_search(page):
	# 个人
	if request.form['customer_type'] == 'Individual':
		individual_customer = SC_Individual_Customer.query.order_by("id").paginate(page, per_page = PER_PAGE)
		return render_template("Information/khxxgl.html",customer=individual_customer)
	# 公司
	else:
		company_customer = SC_Company_Customer.query.order_by("id").paginate(page, per_page = PER_PAGE)
		return render_template("Information/khxxgl.html",customer=company_customer)

# 跳转到新增客户页面
@information.route('/Information/new_customer', methods=['GET'])
def new_customer():
    return render_template("Information/new_customer.html")

# 客户基本信息——公司类
@information.route('/Information/new_company_customer',methods=['GET','POST'])
def new_company_customer():
	if request.method == 'POST':
		SC_Company_Customer(request.form['manager'],request.form['customer_no'],request.form['company_name'],
			request.form['frdb'],request.form['yyzz'],request.form['yyzz_fzjg'],request.form['swdjz'],
			request.form['swdjz_fzjg'],request.form['gszczj'],request.form['gsyyfw'],request.form['gsclrq'],
			request.form['gszclx'],request.form['jbhzh'],request.form['zcdz'],request.form['xdz'],request.form['bgdz'],
			request.form['qtdz'],request.form['education'],request.form['family'],request.form['telephone'],
			request.form['mobile'],request.form['contact_phone'],request.form['email']).add()

		return redirect('Information/khxxgl')

	else:	
	    user = SC_User.query.order_by("id").all()
	    education = SC_Education.query.order_by("id").all()
	    regisiter_type = SC_Regisiter_Type.query.order_by("id").all()

	    return render_template("Information/new_company_customer.html",user=user,
	    	regisiter_type=regisiter_type,education=education)

# 客户基本信息——个人类
@information.route('/Information/new_individual_customer', methods=['GET','POST'])
def new_individual_customer():
	if request.method == 'POST':
		SC_Individual_Customer(request.form['customer_no'],request.form['customer_name'],request.form['manager'],
			request.form['credentials_type'],request.form['credentials_no'],request.form['credentials_org'],
			request.form['credentials_valid'],request.form['sex'],request.form['birthday'],
			request.form['marriage'],request.form['family'],request.form['living_conditions'],
			request.form['position'],request.form['company'],request.form['residence_address'],
			request.form['current_address'],request.form['work_address'],request.form['other_address'],
			request.form['education'],request.form['telephone'],request.form['mobile'],
			request.form['contact_phone'],request.form['email'],request.form['is_active']).add()

		return redirect('Information/khxxgl')

	else:
	    user = SC_User.query.order_by("id").all()
	    credentials_type = SC_Credentials_Type.query.order_by("id").all()
	    living_conditions = SC_Living_Conditions.query.order_by("id").all()
	    education = SC_Education.query.order_by("id").all()

	    return render_template("Information/new_individual_customer.html",user=user,
	    	credentials_type=credentials_type,living_conditions=living_conditions,education=education)

# 编辑客户--公司
@information.route('/Information/edit_company/<int:id>', methods=['GET','POST'])
def edit_company(id):
	customer = SC_Company_Customer.query.filter_by(id=id).first()
	return render_template("Information/edit_company.html",customer=customer)

# 编辑客户--个人
@information.route('/Information/edit_individual/<int:id>', methods=['GET','POST'])
def edit_individual(id):
	customer = SC_Individual_Customer.query.filter_by(id=id).first()
	return render_template("Information/edit_individual.html",customer=customer)
	
# 编辑客户基本信息--公司
@information.route('/Information/edit_company_customer/<int:id>', methods=['GET','POST'])
def edit_company_customer(id):
	if request.method == 'POST':
		customer = SC_Company_Customer.query.filter_by(id=id).first()

		customer.manager = request.form['manager']
		customer.customer_no = request.form['customer_no']
		customer.company_name = request.form['company_name']
		customer.frdb = request.form['frdb']
		customer.yyzz = request.form['yyzz']
		customer.yyzz_fzjg = request.form['yyzz_fzjg']
		customer.swdjz = request.form['swdjz']
		customer.swdjz_fzjg = request.form['swdjz_fzjg']
		customer.gszczj = request.form['gszczj']
		customer.gsyyfw = request.form['gsyyfw']
		customer.gsclrq = request.form['gsclrq']
		customer.gszclx = request.form['gszclx']
		customer.jbhzh = request.form['jbhzh']
		customer.zcdz = request.form['zcdz']
		customer.xdz = request.form['xdz']
		customer.bgdz = request.form['bgdz']
		customer.qtdz = request.form['qtdz']
		customer.education = request.form['education']
		customer.family = request.form['family']
		customer.telephone = request.form['telephone']
		customer.mobile = request.form['mobile']
		customer.contact_phone = request.form['contact_phone']
		customer.email = request.form['email']
		customer.is_active = request.form['is_active']

		customer.update()

		return redirect('xxgl')

	else:
		customer = SC_Company_Customer.query.filter_by(id=id).first()

		regisiter_type = SC_Regisiter_Type.query.order_by("id").all()
		education = SC_Education.query.order_by("id").all()

		return render_template("Information/edit_company_customer.html",customer=customer,
			regisiter_type=regisiter_type,education=education)

# 编辑客户基本信息--个人
@information.route('/Information/edit_individual_customer/<int:id>', methods=['GET','POST'])
def edit_individual_customer(id):
	if request.method == 'POST':
		customer = SC_Individual_Customer.query.filter_by(id=id).first()

		customer.customer_no = request.form['customer_no']
		customer.customer_name = request.form['customer_name']
		customer.manager = request.form['manager']
		customer.credentials_type = request.form['credentials_type']
		customer.credentials_no = request.form['credentials_no']
		customer.credentials_org = request.form['credentials_org']
		customer.credentials_valid = request.form['credentials_valid']
		customer.sex = request.form['sex']
		customer.birthday = request.form['birthday']
		customer.marriage = request.form['marriage']
		customer.family = request.form['family']
		customer.living_conditions = request.form['living_conditions']
		customer.position = request.form['position']
		customer.company = request.form['company']
		customer.residence_address = request.form['residence_address']
		customer.current_address = request.form['current_address']
		customer.work_address = request.form['work_address']
		customer.other_address = request.form['other_address']
		customer.education = request.form['education']
		customer.telephone = request.form['telephone']
		customer.mobile = request.form['mobile']
		customer.contact_phone = request.form['contact_phone']
		customer.email = request.form['email']
		customer.is_active = request.form['is_active']

		customer.update()

		return redirect('xxgl')

	else:
		customer = SC_Individual_Customer.query.filter_by(id=id).first()

		credentials_type = SC_Credentials_Type.query.order_by("id").all()
		living_conditions = SC_Living_Conditions.query.order_by("id").all()
		education = SC_Education.query.order_by("id").all()

		return render_template("Information/edit_individual_customer.html",customer=customer,
			credentials_type=credentials_type,living_conditions=living_conditions,education=education)

# 编辑客户--行业务往来信息
@information.route('/Information/sc_dealings/<belong_customer_type>/<int:belong_customer_value>', methods=['GET','POST'])
def sc_dealings(belong_customer_type,belong_customer_value):
	if request.method == 'POST':
		SC_Dealings(request.form['deal_name'],request.form['deal_description'],
			belong_customer_type,belong_customer_value).add()
		return redirect('xxgl')

	else:
		dealings = SC_Dealings.query.filter_by(belong_customer_type=belong_customer_type,
			belong_customer_value=belong_customer_value).order_by("id").all()
		if belong_customer_type == 'Company':
			customer = SC_Company_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_dealings.html",customer=customer,dealings=dealings)
		else:
			customer = SC_Individual_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_dealings.html",customer=customer,dealings=dealings)
		

# 编辑客户--关系人信息
@information.route('/Information/sc_relations/<belong_customer_type>/<int:belong_customer_value>', methods=['GET','POST'])
def sc_relations(belong_customer_type,belong_customer_value):
	if request.method == 'POST':
		SC_Relations(request.form['relation_no'],request.form['relation_name'],
			request.form['relation_type'],request.form['cgbl'],request.form['business_name'],
			request.form['relation_describe'],belong_customer_type,belong_customer_value).add()
		return redirect('xxgl')

	else:
		user = SC_User.query.order_by("id").all()
		relation_type = SC_Relation_Type.query.order_by("id").all()
		relations = SC_Relations.query.filter_by(belong_customer_type=belong_customer_type,
			belong_customer_value=belong_customer_value).order_by("id").all()
		if belong_customer_type == 'Company':
			customer = SC_Company_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_relations.html",customer=customer,user=user,
				relation_type=relation_type,relations=relations)
		else:
			customer = SC_Individual_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_relations.html",customer=customer,user=user,
				relation_type=relation_type,relations=relations)

# 编辑客户--经营信息
@information.route('/Information/sc_manage_info/<belong_customer_type>/<int:belong_customer_value>', methods=['GET','POST'])
def sc_manage_info(belong_customer_type,belong_customer_value):
	if request.method == 'POST':
		SC_Manage_Info(request.form['business_name'],request.form['industry'],
			request.form['business_description'],request.form['business_type'],request.form['stake'],
			request.form['business_address'],request.form['annual_income'],request.form['monthly_income'],
			request.form['establish_date'],request.form['employees'],request.form['manager_name'],
			request.form['credentials_type'],request.form['credentials_no'],request.form['credentials_org'],
			belong_customer_type,belong_customer_value).add()
		return redirect('xxgl')

	else:
		credentials_type = SC_Credentials_Type.query.order_by("id").all()
		industry = SC_Industry.query.order_by("id").all()
		business_type = SC_Business_Type.query.order_by("id").all()
		manege_info = SC_Manage_Info.query.filter_by(belong_customer_type=belong_customer_type,
			belong_customer_value=belong_customer_value).order_by("id").all()
		if belong_customer_type == 'Company':
			customer = SC_Company_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_manage_info.html",customer=customer,credentials_type=credentials_type,
				industry=industry,business_type=business_type,manege_info=manege_info)
		else:
			customer = SC_Individual_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_manage_info.html",customer=customer,credentials_type=credentials_type,
				industry=industry,business_type=business_type,manege_info=manege_info)

# 编辑客户--资产信息
@information.route('/Information/sc_asset_info/<belong_customer_type>/<int:belong_customer_value>', methods=['GET','POST'])
def sc_asset_info(belong_customer_type,belong_customer_value):
	if request.method == 'POST':
		SC_Asset_Info(request.form['asset_name'],request.form['asset_type'],
			request.form['asset_description'],request.form['asset_position'],request.form['credentials_name'],
			request.form['credentials_no'],request.form['appraisal'],request.form['is_mortgage'],
			request.form['mortgage_amount'],request.form['mortgage_object'],
			belong_customer_type,belong_customer_value).add()
		return redirect('xxgl')

	else:
		asset_type = SC_Asset_Type.query.order_by("id").all()
		asset_info = SC_Asset_Info.query.filter_by(belong_customer_type=belong_customer_type,
			belong_customer_value=belong_customer_value).order_by("id").all()
		if belong_customer_type == 'Company':
			customer = SC_Company_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_asset_info.html",customer=customer,asset_type=asset_type,
				asset_info=asset_info)
		else:
			customer = SC_Individual_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_asset_info.html",customer=customer,asset_type=asset_type,
				asset_info=asset_info)
		
# 编辑客户--财务信息
@information.route('/Information/sc_financial_affairs/<belong_customer_type>/<int:belong_customer_value>', methods=['GET','POST'])
def sc_financial_affairs(belong_customer_type,belong_customer_value):
	if request.method == 'POST':
		SC_Financial_Affairs(request.form['main_supplier'],request.form['main_client'],
			request.form['total_assets'],request.form['stock'],request.form['accounts'],
			request.form['fixed_assets'],request.form['total_liabilities'],request.form['bank_borrowings'],
			request.form['private_borrowers'],request.form['monthly_sales'],request.form['profit'],
			request.form['other_monthly_income'],belong_customer_type,belong_customer_value).add()
		return redirect('xxgl')

	else:
		financial_affairs = SC_Financial_Affairs.query.filter_by(belong_customer_type=belong_customer_type,
			belong_customer_value=belong_customer_value).order_by("id").first()

		if belong_customer_type == 'Company':
			customer = SC_Company_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_financial_affairs.html",customer=customer,financial_affairs=financial_affairs)
		else:
			customer = SC_Individual_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_financial_affairs.html",customer=customer,financial_affairs=financial_affairs)

# 编辑客户--附加信息
@information.route('/Information/sc_other_info/<belong_customer_type>/<int:belong_customer_value>', methods=['GET','POST'])
def sc_other_info(belong_customer_type,belong_customer_value):
	if request.method == 'POST':
		# 先获取上传文件
		f = request.files['attachment']
		fname = f.filename
		f.save(os.path.join(UPLOAD_FOLDER_ABS, fname))

		SC_Other_Info(request.form['info_name'],request.form['info_description'],
			UPLOAD_FOLDER_REL + fname,belong_customer_type,belong_customer_value).add()
		return redirect('xxgl')

	else:
		other_info = SC_Other_Info.query.filter_by(belong_customer_type=belong_customer_type,
			belong_customer_value=belong_customer_value).order_by("id").all()
		if belong_customer_type == 'Company':
			customer = SC_Company_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_other_info.html",customer=customer,other_info=other_info)
		else:
			customer = SC_Individual_Customer.query.filter_by(id=belong_customer_value).first()
			return render_template("Information/sc_other_info.html",customer=customer,other_info=other_info)
        
# 贷款信息管理——贷款信息
@information.route('/Information/dkxx', methods=['GET'])
def dkxx():
    return render_template("Information/dkxx.html")

# 贷款信息管理——贷款信息(还款记录)
@information.route('/Information/dkxx_hkjl', methods=['GET'])
def dkxx_hkjl():
    return render_template("Information/dkxx_hkjl.html")

# 贷款信息管理——贷款信息(还款记录明细)
@information.route('/Information/dkxx_hkjlInfo', methods=['GET'])
def dkxx_hkjlInfo():
    return render_template("Information/dkxx_hkjlInfo.html")

# 贷款信息管理——贷款信息(贷后变更)
@information.route('/Information/dkxx_dhbg', methods=['GET'])
def dkxx_dhbg():
    return render_template("Information/dkxx_dhbg.html")

# 贷款信息管理——贷款信息(贷后变更——修改还款计划)
@information.route('/Information/dkxx_dhbg_xghkjh', methods=['GET'])
def dkxx_dhbg_xghkjh():
    return render_template("Information/dkxx_dhbg_xghkjh.html")

# 贷款信息管理——贷款信息(贷后变更——修改担保人)
@information.route('/Information/dkxx_dhbg_xgdbrsj', methods=['GET'])
def dkxx_dhbg_xgdbrsj():
    return render_template("Information/dkxx_dhbg_xgdbrsj.html")

# 贷款信息管理——贷款信息(贷后变更——修改共同借款人)
@information.route('/Information/dkxx_dhbg_xggtjkr', methods=['GET'])
def dkxx_dhbg_xggtjkr():
    return render_template("Information/dkxx_dhbg_xggtjkr.html")

# 贷款信息管理——贷款信息(贷后变更——修改抵质押信息)
@information.route('/Information/dkxx_dhbg_xgdzyxx', methods=['GET'])
def dkxx_dhbg_xgdzyxx():
    return render_template("Information/dkxx_dhbg_xgdzyxx.html")