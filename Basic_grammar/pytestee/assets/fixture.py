import pytest

@pytest.fixture()
def before():
    print('\nbfefore each test')

def test_1(before):
    print('test_1')


def test_2(before):
    print('test_2')


if __name__ == '__main__':
    pytest.main('-s fixture.py')