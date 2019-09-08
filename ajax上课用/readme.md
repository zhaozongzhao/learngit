#说明:上课讲ajax前后台交互的用的简易后台


- 环境安装：pip install flask

- 项目运行  直接运行 http_server.py文件
- 接口说明
    - 首页地址：127.0.0.1：5000

    - 接口1:/login :登录接口
        - 参数：user--->账号  pwd-->密码
        - 请求方法：post 
        - 返回数据 json类型

    - 接口2：/pro_list：获取项目列表
        - 无参数，
        - 请求方法:get
        - 返回数据：所有项目列表，json类型
    
    - 接口3：/interface :获取接口列表
        - 参数：pro_id :  str类型
        - 请求方式：post
        - 返回数据：对应项目的所有接口，json类型


    - 返回数据格式
    {   
    code：状态码,  0代表失败，1代表成功
    data:数据,   
    msg:说明信息
     }


