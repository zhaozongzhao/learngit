import pytest

@pytest.fixture()
def before():
    print('测试类')


# #调用方式一
# @pytest.mark.usefixtures('before')
# def test_1():
#     print('test_1')
#
# @pytest.mark.usefixtures('before')
# def test_2():
#     print('test_2')
#
#
# class Test1:
#
#     @pytest.mark.usefixtures('before')
#     def test_3(self):
#         print('test_3')

@pytest.mark.usefixtures('before')
class Test2:

    def test_5(self):
        print('5')

    def test_6(self):
        print('6')

if __name__ == '__main__':
    pytest.main('-s fixture_2.py')