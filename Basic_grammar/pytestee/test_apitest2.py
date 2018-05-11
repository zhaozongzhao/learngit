import pytest
import requests

class TestApiVex2(object):
    domain = 'https://www.v2ex.com/'

    @pytest.mark.parametrize('name,id',[('python',90),('java',63),('nodejs',436)])
    def test_node(self,name,id):
        path ='api/nodes/show.json?name={}'.format(name)
        url = self.domain + path
        res = requests.get(url).json()
        assert res['name'] == name
        assert  res['id'] == id




if __name__ == '__main__':
    pytest.main(["--html=test_one_func.html"])
