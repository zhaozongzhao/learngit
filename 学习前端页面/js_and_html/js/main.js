// window.onload{


// }
$(function(){
  // 选择元素绑定点击操作
  $('.li1').click(
    function(){
      // $(this)当前元素本身
       $(this).next().toggle().siblings('div').hide();
      
    }
  )
  // jquery操作元素属性
  $('a').attr('href','http://www/baidu.com')
  $('a').removeAttr('href');
  
  // 样式操作
  var conent = $('.conent')
  conent.addClass('hied');
  conent.removeClass('hied');
  
  // 文件操作
  console.log(conent.text())
  console.log(conent.html())
  console.log(conent.val())



})