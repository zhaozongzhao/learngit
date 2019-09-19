<template>
  <table class="box">
      <tr >
          
          <th v-for="(item, key) in project_handers" v-bind:key="key" >{{item}}</th>
         
        </tr>
        <!-- v-bind 缩写为： -->
      <tr v-for="(item1 , key) in  projieces" :key="key">
          <td>{{item1.name}}</td>
          <td>{{item1.leader}}</td>
          <td>{{item1.app_name}}</td>
         
      </tr>
      

  </table>
</template>

<script>
export default {
    name: 'Projecttable',
    data(){

     return{
         project_handers:['项目名称','项目负责人','P2P平台'],
         projieces:[
             {name:'前程贷',leader:'笨笨',app_name:'平台应用'},
             {name:'前程贷',leader:'笨笨',app_name:'平台应用'},
             {name:'前程贷',leader:'笨笨',app_name:'平台应用'},
         ]
     }
    }

}
</script>

<style>
 .box{
     color: blue;
     margin: 50px auto;
     padding: 2px;
     
 }
 td,th{
     border: 1px solid #dddddd;
 }

</style>