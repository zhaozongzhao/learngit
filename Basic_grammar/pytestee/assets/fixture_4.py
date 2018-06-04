import time
import pytest

@pytest.fixture(scope='function',autouse=True)
def mod_header():
    print('\n测试类')

def test_one():
    print('in test_one()')

def test_two():
    print('in test_two()')

if __name__ == '__main__':
    pytest.main('-s fixture_4.py')