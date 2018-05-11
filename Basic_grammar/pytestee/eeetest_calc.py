import pytest

def add(x,y):
    return x+y

def test_add():
    assert add(1,0)  ==  1
    assert add(1,1)  ==  2
    assert add(1,99) == 100


def f():
    return 4

def test_function():
    assert f() == 4


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1/0


def test_recursion_depth():
    with pytest.raises(RuntimeError) as excinfo:
        def f():
            f()
        f()
    assert 'maximum recursion' in str(excinfo.value)



