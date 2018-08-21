
from configparser import ConfigParser

class ParsePageObjectRepository(object):

    def __init__(self,config_path):

        self.cf = ConfigParser() #生成解析器
        self.cf.read(config_path)

    def getItemSection(self,sectionName):
        return dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)



if __name__ == '__main__':
    pp = ParsePageObjectRepository('/Users/hnbl009/gitfile/learngit/Basic_grammar/配置文件/test.ini')
    print(pp.getItemSection('config'))
    print(pp.getOptionValue('config','platformname'))