import configparser

# /Users/hnbl009/gitfile/learngit/Basic_grammar/配置文件/test.ini

cf = configparser.ConfigParser() #实例化
path = '/Users/hnbl009/gitfile/learngit/Basic_grammar/配置文件/test.ini'
cf.read(path) #读取配置文件

print(cf.options('config')) #返回所有键的序列

print(cf.get('config','platformName')) #返回项目对应键的值

print(cf.sections()) #获取所有项目名称

print(cf.items('config'))
#
# cf.add_section('回话2')
# cf.set('回话2','platformName','ios')
# cf.write(open(path,'w'))