<template>
  <div>
    <el-table
    class="box"
    :data="tableData"
    style="width: 370px"
     >
    <el-table-column
      fixed
      prop="date"
      label="日期"
      width="150">
    </el-table-column>
    <el-table-column
      prop="name"
      label="姓名"
      width="120">
    </el-table-column>
    <el-table-column
      fixed="right"
      label="操作"
      width="100">
      <template slot-scope="scope">
        <el-button @click.native.prevent="deleteRow(scope.$index, tableData)" type="text" size="small">删除</el-button>
        <el-button @click.native.prevent="editrow(scope.$index,tableData)" type="text" size="small" @click = "name = '正在编辑'">{{name}}</el-button>
      </template>
    </el-table-column>
  </el-table>

  </div>
</template>

<script>
export default {
     name : 'Newtable2',
    data() {
      return {
        tableData: [{
          date: '2016-05-02',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1518 弄',
          zip: 200333
        }, {
          date: '2016-05-04',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1517 弄',
          zip: 200333
        }, {
          date: '2016-05-01',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1519 弄',
          zip: 200333
        }, {
          date: '2016-05-03',
          name: '王小虎',
          province: '上海',
          city: '普陀区',
          address: '上海市普陀区金沙江路 1516 弄',
          zip: 200333
        }],
        name:'编辑',
      }
    },
    methods : {
      deleteRow(index, rows) {
        rows.splice(index, 1);
      },
      editrow(index,rows){
        //   this.name = '已编辑'
          alert([rows.date,rows.name,rows.address])
      }


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
