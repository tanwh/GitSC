// 动态创建表单
function createForm(action,arr){
    var tmpForm = $("<form action='"+action+"' method='POST'></form>");
    for(var key in arr) {
        tmpForm.append("<input type='hidden' value='"+arr[key]+"' name='"+key+"'/>");
    }
    tmpForm.appendTo(document.body).submit();
}

//日历
function datepicker(){
		var dateFormat = $('.datepicker').datepicker('option', 'dateFormat');
		$('.datepicker').datepicker({ dateFormat: 'yy-mm-dd' });		
		$('.datepicker').datepicker('option', 'dateFormat', 'yy-mm-dd');		
}

//iframe自适应高度用于iframe内部页面			
function Frame(){
	var content_iframe = $('#content_frame',window.parent.document);//获取iframeID
    var height = parseInt($(".content").height())+20;//使iframe高度等于子网页高度	
    content_iframe.height ( height < 500 ? 500 : height);
}

//iframe自适应高度用于主页面
function resizeFrame(id){
	var height = $('#'+id).contents().find(".content").height();
    if(id=="content_frame"){        
        $('#'+id).height( height < 500 ? 500 :height+40);
    }
    else{
        $('#'+id).height(height+20);
    }
    
    //if(id=='content_frame')
	   //$('#'+id).height(height < 500 ? 500 : height+40);
   // else
       //$('#'+id).height(height+20); 
}

//左侧leftmenu样式变换
function leftmenu(obj){
	var leftmenu=$("li[id]")//*注意IE6不识别属性选择器*
	for(i=0;i<leftmenu.length;i++)
		leftmenu[i].className="";
	obj.className="active";	
}

//切换iframe里的内容用于主页面
function changeiframe(page){
	$("#content_frame").attr("src",page);
}

//切换iframe里的内容用于iframe内部页面	
function iframe(page){
	window.location.href = "/" + page;
   // alert(window.location.href);
}

//切换iframe里的内容用于二级iframe内部页面  
function doubleiframe(page){
    window.parent.window.location.href = "/" + page;   
}

//选中表格行
function changeColor(obj){
    if(obj.checked==true)
        obj.parentElement.parentElement.style.background="#def0d8"
    else
        obj.parentElement.parentElement.style.background="#efefef"
}

//反选按钮
function ChkAllClick(){
    var arrSon = document.getElementsByName("checkbox");
    for(i=0;i<arrSon.length;i++) {
        if(arrSon[i].checked!=true)
            arrSon[i].click();
        else
            arrSon[i].click();
    }
}

/**
 * 显示时间
 */
function showdate()
{
    var date=new Date();
    var month=creattime(date.getMonth()+1);
    var da=creattime(date.getDate());
    var day=date.getDay();
    var nian=date.getFullYear();
    var txt;
    function creattime(i)
    {
        if(i<10)
        {i="0"+i}
        return i
    }
    switch(day)
    {
        case 1:
            txt="一"
            break
        case 2:
            txt="二"
            break
        case 3:
            txt="三"
            break
        case 4:
            txt="四"
            break
        case 5:
            txt="五"
            break
        case 6:
            txt="六"
            break
        case 0:
            txt="日"
            break
        default:
            sj.innerHTML="出错了"
    }
    document.getElementById('date').innerHTML=nian+"年"+month+"月"+da+"日&nbsp;&nbsp;&nbsp;星期"+txt
}

//tab标签页
function selectTag(showContent,selfObj){
	// 操作标签
	var tag = document.getElementById("tags").getElementsByTagName("li");
	var taglength = tag.length;
	for(i=0; i<taglength; i++){
		tag[i].className = "";
	}
	selfObj.parentNode.className = "selectTag";
	// 操作内容
	for(i=0; j=document.getElementById("tagContent"+i); i++){
		j.style.display = "none";
	}
	$("#"+showContent).show();
    Frame();
}
function tab(showContent,id,selfObj){    
    var tag = document.getElementById(id).getElementsByTagName("li");
    var taglength = tag.length;
    for(i=0; i<taglength; i++){
        tag[i].className = "";
    }
    selfObj.parentNode.className = "selectTag";
    $('.tab').hide();
    $('#'+showContent).show();
}
function thirdTb(showContent,id,selfObj){    
    var tag = document.getElementById(id).getElementsByTagName("li");
    var taglength = tag.length;
    for(i=0; i<taglength; i++){
        tag[i].className = "";
    }
    selfObj.parentNode.className = "selectTag";
    $('.thirdTb').hide();
    $('#'+showContent).show();
}
//控制div的显示和隐藏
function changeDiv(show_div,hide_div){
    $("#"+show_div).show();
    $("#"+hide_div).hide();
    Frame();
}

//信贷员搜索用来赋值
function get_name(obj,idText,idValue){
    var tr=obj.parentElement.parentElement
    var td=tr.getElementsByTagName("td");
    $("#" + idText).val(td[2].innerHTML);
    $("#" + idValue).val(td[1].innerHTML);
    $(".display-div").hide();    
}
//双层Iframe内部
function doubleIframe(frameid){
    var content_iframe = $('#'+frameid,window.parent.document);//获取iframeID
    var height = parseInt($(".content").height())+60;//使iframe高度等于子网页高度 
    content_iframe.height(height);
    var iframe= $('#content_frame',window.parent.parent.document);
    var height1 = parseInt($(".content",window.parent.document).height())+40;
    iframe.height(height1);
}
//3层Iframe内部
function thirdIframe(parentIframe,grandIframe){
    var content_iframe1 = $('#'+parentIframe,window.parent.document);//获取iframeID
    var height1 = parseInt($(".content").height())+60;//使iframe高度等于子网页高度 
    content_iframe1.height(height1);

    var content_iframe2 = $('#'+grandIframe,window.parent.parent.document);//获取iframeID
    var height2 = parseInt($(".content").height())+60;//使iframe高度等于子网页高度 
    content_iframe2.height(height2);

    var iframe= $('#content_frame',window.parent.parent.parent.document);
    var height3 = parseInt($(".content",window.parent.parent.document).height())+40;
    iframe.height(height3);
}
// //***************表单元素封装**********************
// function formBox(){  
// //申请信息
//     var sqxx="<table class='table-list'>"+               
//         "<tr>"+
//             "<td class='table-label'>申请金额（元）*</td>"+
//             "<td><input type='text' id=''/></td>"+
//             "<td class='table-label'>申请期限（月）*</td>"+
//             "<td><input type='text' id=''/>月</td>"+
//             "<td class='table-label'>分期还款额(元)*</td>"+
//             "<td><input type='text' id=''/></td>"   +                   
//         "</tr>"+
//         "<tr>"+
//             "<td class='table-label'>贷款用途*</td>"+
//             "<td>"+
//                 "<select>"+
//                     "<option>---请选择---</option>"+
//                     "<option>流动资金贷款</option>"+
//                 "</select>"+
//             "</td>"+
//             "<td class='table-label'>详细说明</td>"+
//             "<td colspan='3'><input type='text' id='' class='long'/></td>"+               
//         "</tr>"+
//         "<tr>"+
//             "<td class='table-label'>贷款原因</td>"+
//             "<td colspan='5'><input type='text' id='' class='long'/></td>"+                           
//         "</tr>"+
//     "</table>";
//     $(".sqxx").html(sqxx); //申请信息          
// }