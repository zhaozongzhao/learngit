// template展示给用户看，想当于MVVM中的V
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 在父组件中给子组件传值 -->
    <HelloWorld msg="学习VUE"/>
     <greeting/>
     <study/>
     <projiecttable/>
     <element_study/>
  </div>
</template>

<script>
// 导入子组件
import HelloWorld from './components/HelloWorld.vue'
import greeting from './components/greeting.vue'
import study from './components/study.vue'
import  Projiecttable  from './components/Prijecttable.vue'
import Element_studt from './components/Elementui_study.vue'

export default {
  // 定义组件名称
  name: 'app',
  components: {  //声名子组件
    HelloWorld,
    greeting,
    study,
    Projiecttable,
    Element_studt,
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
