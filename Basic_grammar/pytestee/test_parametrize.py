import pytest
#test_eval方法中传入了2个参数，就如同@pytest.mark.parametrize装饰器中定义的那样，因此简单理解，
# 我们可以把parametrize装饰器想象成是数据表格，有表头(test_input,expected)以及具体的数据。
@pytest.mark.parametrize('test_input,expected',[("3+5",8),("2+4",6),("6*9",42)])
def test_eval(test_input,expected):
    assert eval(test_input) == expected