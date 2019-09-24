
<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <h2>{{title}}</h2>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  props: { //从父组件中传入数据
    msg: String,
    title : Number,
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
