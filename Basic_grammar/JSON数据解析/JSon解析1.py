import json
data = {
    'no' : 1,
    'name' : 'Runoob',
    'url'  : 'http://www.runoob.com'

}

#将字典改为json
json_str = json.dumps(data)
print('python原始数据',repr(data))
print('Json对象',json_str)


#将json改变为字典
data2 = json.loads(json_str)
print('data2',data2['name'])
print('dats2',data2['url'])

# 写入 JSON 数据
with open('data.json', 'w') as f:
    json.dump(data, f)

# 读取数据
with open('data.json', 'r') as f:
    data = json.load(f)