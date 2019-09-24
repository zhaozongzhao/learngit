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
           message:'hello Vue学习菜鸟11'
       }
    },
    created(){
      console.log('实例创建之后，能获取到this')
      console.log('username: ',this.message)
    },
    mounted(){
      console.log('vue实例挂载到DOM树之后')
    }
}
</script>
// 样式
<style scoped>
   p{
     color : red;
 }

</style>