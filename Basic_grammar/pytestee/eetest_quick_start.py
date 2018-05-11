def reverse(string):
    return string[::-1]



def test_reverse():
    strinng = 'good'
    assert reverse(strinng)=='doog'

    another_string = 'itest'
    assert reverse(another_string) == 'tseti'