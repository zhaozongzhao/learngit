
  <!-- <el-table是elenium提供的组件 -->

<template>
    <div>

     <el-table
    ref="multipleTable"
    :data="tableData"
    tooltip-effect="dark"
    style="width: 100%" 
   
    @selection-change="handleSelectionChange">
    <el-table-column
      type="selection"
      width="55">
    </el-table-column>
    <el-table-column
      label="项目名称"
      width="120"
      prop="name">
      <!-- <template slot-scope="scope">{{ scope.row.date }}</template> -->
      
    </el-table-column>
    <el-table-column
      
      prop="leader"
      label="项目负责人"
      width="120">
    </el-table-column>
    <el-table-column
      prop="app_name"
      label="项目地址"
      width="300"
      >
    </el-table-column>
  </el-table>
    <div style="margin-top: 20px">
    <el-button @click="toggleSelection([tableData[1], tableData[2]])">切换第二、第三行的选中状态</el-button>
   
  </div>


    </div>
  </template>

<script>

  export default {
    name : 'Newtable',
    data() {
      return {
        tableData:[
             {name:'前程贷',leader:'笨笨',app_name:'平台应用'},
             {name:'前程贷',leader:'笨笨',app_name:'平台应用'},
             {name:'前程贷',leader:'笨笨',app_name:'平台应用'},
         ],
        multipleSelection: [],
      
      }
    },
    methods: {
     handleSelectionChange(val) {
        this.multipleSelection = val;
        console.log(this.multipleSelection);
      },
      toggleSelection() {
        this.$refs.multipleTable.toggleRowSelection();
    
      },
      
      
    }
  }
</script>
<style scoped>
   .box{
     /* background:red; */
     margin: 50px 500px;
     width:100px;  

   }
</style>