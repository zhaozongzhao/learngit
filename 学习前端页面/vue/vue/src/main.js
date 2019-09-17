
//导入vue.js
import Vue from 'vue'
//导入app.vue根组件
import App from './App.vue'

Vue.config.productionTip = false

new Vue({
  render: h => h(App),//渲染app根组件
}).$mount('#app')
