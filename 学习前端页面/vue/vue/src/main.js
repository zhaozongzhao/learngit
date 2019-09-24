
//导入vue.js
import Vue from 'vue'
// 导入ElemenUI
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
// 导入子组件
import greeting from './components/greeting.vue';
// 创建全局组件
Vue.component('greeting',greeting);

//导入app.vue根组件
import App from './App.vue';

// Vue.component(id='hello-word',HelloWorld)
// 加载ElementUI ,必须在实例之前加入
Vue.use(ElementUI);

Vue.config.productionTip = false

new Vue({
  render: h => h(App),//渲染app根组件
}).$mount('#app')
