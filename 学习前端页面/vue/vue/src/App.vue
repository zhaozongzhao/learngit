// template展示给用户看，想当于MVVM中的V
<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- 在父组件中给子组件传值 -->
    <HelloWorld msg="学习VUE"/>
     <greeting/>
  </div>
</template>

<script>
// 导入子组件
import HelloWorld from './components/HelloWorld.vue'
import greeting from './components/greeting.vue'

export default {
  // 定义组件名称
  name: 'app',
  components: {  //声名子组件
    HelloWorld,
    greeting
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
