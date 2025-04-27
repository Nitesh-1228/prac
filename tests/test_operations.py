from src.math_operations import mul,add

def test_mul():
    assert mul(2,3)==6
    assert mul(-3,3)==-9
    assert mul(9,0)==0
def test_add():
     assert add(9,0)==9
     assert add(-9,8)==-1
     assert add(8,2)==10
