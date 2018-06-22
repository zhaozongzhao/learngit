import pytest




# @pytest.mark.usefixtures('before')
# class Test2(object):
#
#     def test_5(self):
#         print('5')
#
#     def test_6(self):
#         print('6')

@pytest.mark.usefixtures('before')
class Test2:

    def test_5(self):
        print('5')
        assert 0

    def test_6(self):
        print('6')
        assert 0



