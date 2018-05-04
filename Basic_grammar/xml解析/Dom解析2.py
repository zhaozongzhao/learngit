import xml.etree.ElementTree as ET
import os
import sys

#遍历xml节点
def traverseXml(element):
    if len(element)>0:
        for child in element:
            print(child.tag,'----',child.attrib)
            traverseXml(child)


if __name__ == '__main__':
    xmlFilePath = os.path.abspath('test.xml')
    print(xmlFilePath)
    try:
        tree = ET.parse(xmlFilePath)
        print('tree type',type(tree))

        #获取节点
        root = tree.getroot()
    except Exception as  e:
        print('parse test.xml fail')
        sys.exit()

    print('root  type ',type(root))
    print(root.tag,'----',root.attrib)

    #遍历下一层
    for child in root:
        print('遍历root下一层',child.tag,'-----',child.attrib)

    #使用下标访问

    print(root[0].text)
    print(root[1][1][0].text)

    print (20 * "*")
    #遍历xml文件
    traverseXml(root)
    print (20 * "*")


    #格局标签名查找root下的所有标签
    captionlist = root.find('item')
    print(len(captionlist))

    for caption in captionlist:
        print(caption.tag,'----',caption.attrib)


    #修改xml文件,将password修改9999
    login = root.find('login')
    passwordvalue = login.get('password')
    login.set('password','9999999')
    print(login.get('password'))



