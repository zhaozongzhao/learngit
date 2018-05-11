import pytest
import json
import smtplib

class TestUserPassword(object):
    @pytest.fixture
    def users(self):
        return json.loads(open('./users.dev.json', 'r').read())

    # @pytest.fixture(scope='module')
    # def smtp(self):
    #     smtp = smtplib.SMTP('smtp.gmail.com',587,timeout=5)
    #     yield smtp
        smtp.close()

    def test_user_password(self,users):
        #遍历每天user数据
        for user in users:
            passwd = user['password']
            assert len(passwd) >=6
            msg = 'user {} has a weak password'.format(user['name'])
            assert  passwd != 'password',msg
            assert  passwd != 'password123',msg

