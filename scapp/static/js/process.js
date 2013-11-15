//-----------------------新增贷款申请--------------------------------------
//获取客户信息
function getCustomer(obj){
	var tr=obj.parentElement.parentElement;
	var td=tr.getElementsByTagName("td");
	var id1=$('#dksq_info').contents().find("#customer_no");
	var id2=$('#dksq_info').contents().find("#customer_name");
	$(id1).text(td[1].innerHTML);
	$(id2).text(td[2].innerHTML);
	$('#dksq_info').show();
	$('#search').hide();
	Frame();    		
}
//-----------------------现金流分析--------------------------------------
//业务历史&业务展望切换
function xjlfx(obj){
    if(obj.options[obj.selectedIndex].value==0){
        $("#ywls").show();
        $("#ywzw").hide();
    }
    if(obj.options[obj.selectedIndex].value==1){
        $("#ywzw").show();
        $("#ywls").hide();
    }
}
//----------------------贷款申请信息--------------------------
//表格添加行
function addTd(table,frameid){
    if(table=="haveCredit"){//是否申请过贷款
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");      
    }
    if(table=="sfwtrdb"){//是否为他人担保
        $("#"+table).append("<tr class='add'><td><input type='text' id='' /></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");      
    }
     if(table=="ywdyw"){//有无抵押物
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td></tr>");      
    }
    if(table=="dbInformation"){//担保信息
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");
    }
	if(table=="xdls"){//信贷历史
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");
    }
	if(table=="gtjkr"){//共同借款人
        $("#"+table).append("<tr class='add'><td><select id=''  style='width:80px;'></select></td><td><span id=''></span></td><td><span id=''></span></td><td><span id=''></span></td><td><input type='text' id='' style='width:100px;'/></td><td><input type='text' id='' style='width:130px;'/></td><td><input type='text' id='' style='width:90px;'/></td><td><input type='text' id='' style='width:90px;'/></td></tr>");
    }
    if(table=="dbr"){//担保人
        $("#"+table).append("<tr class='add'><td><select id=''  style='width:80px;'></select></td><td><span id=''></span></td><td><span id=''></span></td><td><span id=''></span></td><td><input type='text' id='' style='width:100px;'/></td><td><input type='text' id='' style='width:130px;'/></td><td><input type='text' id='' style='width:90px;'/></td><td><input type='text' id='' style='width:90px;'/></td></tr>");
    }
    if(table=="jydyw"){//建议抵押物
        $("#"+table).append("<tr class='add'><td><select id=''  style='width:120px;'></select></td><td><input type='text' id=''  class='tbInput'/></td><td><input type='text' id=''  class='tbInput'/></td><td><input type='text' id=''  class='tbInput'/></td><td><input type='text' id=''  class='tbInput'/></td><td><input type='text' id=''  class='tbInput'/></td><td><input type='checkbox' id=''/></td></tr>");
    }
    if(table=="yfzk"){//现金及银行存款&应付账款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="yszk"){//应收账款&预收账款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="yfkx"){//预付款项&短期借款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="ch"){//存货&社会集资
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="gdzc"){//固定资产&长期借款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="qt"){//其他经营资产&其他
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }    
    if(table=="sr"){//收入
        $("#"+table).append("<tr class='add'><td style='width:166px;'><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="kbcb"){//可变成本
        $("#"+table).append("<tr class='add'><td style='width:166px;'><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="qtfy"){//其他费用
        $("#"+table).append("<tr class='add'><td style='width:166px;'><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="qtzc"){//其他支出
        $("#"+table).append("<tr class='add'><td style='width:166px;'><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="qtsr"){//其他收入
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="zyywlrfx"){//主营业务利润分析
        $("#"+table).append("<tr class='add'><td><input type='text' id='' style='width:100px;'/></td><td><input type='text' id='' style='width:100px;'/></td><td><input type='text' id='' style='width:100px;'/></td><td><input type='text' id='' style='width:100px;'/></td><td><input type='text' id='' style='width:100px;'/>%</td><td><input type='text' id='' style='width:100px;'/>%</td></tr>");
    }
//----------------------基本情况--------------------------
    if(table=="zxjl"){//征信记录
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");
    }
    if(table=="wtrdbqk"){//为他人担保情况
        $("#"+table).append("<tr class='add'><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td><td><input type='text' id='' class='tbInput'/></td></tr>");
    }
 //----------------------资产负债表--------------------------   
    if(table=="ck"){//存款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="yhcshp"){//未到期的银行程税汇票
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="Yszk"){//应收账款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }    
    if(table=="Ch"){//存货(元)
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }  
    if(table=="fdc"){//固定资产-房地产
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }  
    if(table=="sb"){//固定资产-设备
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="cl"){//固定资产-车辆
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }   
    if(table=="Qtjyzc"){//其它经营资产(元)
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="bwzc"){//其它非经营资产或表外资产
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="yfgyszk"){//应付供货商账款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="qtyfzk"){//其他应付帐款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="yszky"){//预收账款(元)
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="dqyhjk"){//短期银行借款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="dqshjz"){//短期社会集资
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="cqyhjk"){//长期银行借款
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="cqshjz"){//长期社会集资
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
    if(table=="qtbwfz"){//其他表外负债
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    }
//----------------------损益情况分析--------------------------
    if(table=="jysr"){//经营收入
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="Kbcb"){//可变成本
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="qtcb"){//其他成本
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="qtcb2"){//其他成本2
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
    if(table=="yjmlzh"){//主要经营项目月均毛利组合分析
        $("#"+table).append("<tr class='add'><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td></tr>");
    } 
//----------------------现金流分析--------------------------
    if(table=="qtfyx"){//其他费用息
        $("#"+table).append("<tr class='add'><td style='width:225px'><input type='text' id='' style='width:80%'/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td style='width:80px'>0</td></tr>");
    } 
    if(table=="qtjk"){//其他借款
        $("#"+table).append("<tr class='add'><td style='width:225px'><input type='text' id='' style='width:80%'/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td style='width:80px'>0</td></tr>");
    } 
    if(table=="chqtjk"){//偿还其他借款
        $("#"+table).append("<tr class='add'><td style='width:225px'><input type='text' id='' style='width:80%'/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td style='width:80px'>0</td></tr>");
    }
    if(table=="qtjkxjly"){//其他借款现金来源
        $("#"+table).append("<tr class='add'><td style='width:225px'><input type='text' id='' style='width:80%'/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td><input type='text' id=''/></td><td style='width:80px'>0</td></tr>");
    }
    doubleIframe(frameid);
}
//表格删除行
function removeTd(table,frameid){   
    //var tr=$("#"+table+' .add')
    //tr.each(function (i){       
       // if(i==tr.length-1)
           // this.remove();
   // });
    var tr= document.getElementById(table).getElementsByTagName("tr");
    if(tr[tr.length-1].className=="add"){//至少要保留一行
        document.getElementById(table).deleteRow(tr.length-1);//删除最后一行
    }
    doubleIframe(frameid);
}
