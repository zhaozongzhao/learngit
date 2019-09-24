<template>
  <div class="login">
        <!-- <form action="" method="post">
            <label for="uaername">用户名:</label>
            <input type="text" id="username" placeholder="请输入用户名" v-model= 'username'><br>
            <label for="pass">密&nbsp;&nbsp;&nbsp;码:</label>
            <input type="password" id="pass" placeholder="请输入密码" v-model = 'password'><br>

        </form> -->

 <el-form :model="ruleForm" status-icon :rules="rules" ref="ruleForm" label-width="100px" 
 class="demo-ruleForm" :label-position="labelPosition">
    
          <el-form-item label="用户名" prop="username">
             <el-input type="text" v-model="ruleForm.username" autocomplete="off"></el-input>
          </el-form-item>
          <el-form-item label="确认密码" prop="password">
              <el-input type="password" v-model="ruleForm. password" autocomplete="off"></el-input>
          </el-form-item>
  
</el-form>
  </div>
</template>

<script>
export default {
    name:'login',
    data(){
        return{
            // username : '111',
            // password : '222',
             labelPosition:'right',
             ruleForm: {
                  username : '111',
                  password : '222',
        
          }
        }
    }

}
</script>

<style>
  /* input{
      margin: 10px auto;
      font-size: medium;
    
  }
  label{
      margin-right: 10px ;
  } */
  .el-form{
      width: 300px;
      margin: 50px auto;
  }
</style>