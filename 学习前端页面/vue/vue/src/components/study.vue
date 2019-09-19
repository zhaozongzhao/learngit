<template>
   <div>
       <!-- 插值表达式 -->
      <p>{{name}}{{message1}}</p> 
      <!-- v-开头为VUE中的指定有特殊含义，v-bind绑定属性值 -->
      <span v-bind:title="dream">小目标</span>
      <P v-if="isnot">判断显示</P>
      <P v-show="show">show显示</P>
   </div>
</template>

<script>
export default {
    name:'study',
    data(){
        return{
            message1:'学习努力学习vue',
            name:'zzz',
            dream :'小目标',
            isnot:false,
            show:false,

        }

    }

}
</script>

<style>

</style>