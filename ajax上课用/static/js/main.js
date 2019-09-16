$(function(){
  
//   给提交按钮绑定点击事件
  $('dl').click(function(){
    //   获取账号密码
      var user = $('#username').text();
      var pwd = $('password').text();
      $.ajax({
          type : 'post',
          usl :'/login',
          data :{"user":user,"pwd":pwd},
        //   请求数据类型÷
          contentType:JSON,
        //   返回数据类型
          dataType:JSON,
      }).done(function(data){
          console.log(data)
      }).fail(function(){
          alert('请求失败')
      })



  })
      
})