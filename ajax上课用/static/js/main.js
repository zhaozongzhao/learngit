$(function(){
  
//   给提交按钮绑定点击事件
  $('#dl').click(function(){
    //   获取账号密码
      var user = $('#username').val();
      var pwd = $('#password').val();
      $.ajax({
          type : 'post',
          url :'/login',
          data :{"user":user,"pwd":pwd,'token':'11'},
        //   返回数据类型
          dataType:"json",
      }).done(function(data){
          console.log(data)
          if(data.code ==="1"){
            alert('登陆成功跳转至首页');
          }
          else{
            alert(data.msg);

          }
      }).fail(function(){
          alert('请求失败')
      })



  })

  // 当项目加载完毕之后，发送ajax请求获取页面上的项目列表
  $.ajax(
   {
    type : "get",
    url : "/pro_list",
    // dataType : "json",
    dataType:'json',

   }
  ).done(function(data){
    // 判断业务码是否成功
       if (data.code === "1"){
        //  将项目数据加载的页面
         var res = data.data;
         console.log(res);
         for( i in res){
           console.log(res[i].title);
            //  选中项目的选择框
            var option = '<option value="'+res[i].id+'">'+res[i].title +'</option>';
            $("#pro").append(option);
         }

       }
       else{

       alert("加载失败");
      }

  }).fail(function()
    {
      alert('sss');
  }
  )
 })     
  // 当页面上的选项选择了之后，那么选择该项目下的接口
 $(document).on('change', '#pro', function(){
      $.ajax(
        {
        url:'/interface',
        data:{'pro_id':$(this).val()},
        dataType:'json',
        method:'post',
      }
      ).done(function(data){
       // 判断业务码是否成功
       if (data.code === "1"){
        //  清空接口选择框中原来的数据
        $("#interface").empty();
        //  将项目数据加载的页面
         var res = data.data;
         console.log(res);
         for( i in res){
           console.log(res[i].title);
            //  选中项目的选择框
            var option = '<option value="'+res[i].id+'">'+res[i].name +'</option>';
            $("#interface").append(option);
         }

       }
       else{

       alert("加载失败");
      }

        
      })

  })

