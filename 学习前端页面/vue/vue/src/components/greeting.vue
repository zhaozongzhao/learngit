 <!-- 展示给用户看得   -->
<template>
  <div>
       <!-- 插值表达式 -->
      <p>{{message}}</p>
  </div>
</template>
<script>
// 数据
export default {
    name : 'geeting',
    data(){
       return {
           message:'hello Vue学习菜鸟'
       }
    }
}
</script>
// 样式
<style scoped>
   p{
     color : red;
 }

</style>