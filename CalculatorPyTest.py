from Calculator import Calculator

calculator = Calculator()

def test_add():
    assert calculator.add(2,2) == 4
    assert calculator.add(3,1.3) == 4.3

def test_minus():
    assert calculator.minus(2,4) == -2
    assert calculator.minus(0,4.2) == -4.2

def test_multiple():
    assert calculator.multiple(5,2) == 10
    assert calculator.multiple(3.3,2) == 6.6

def test_devide():
    assert calculator.devide(9,3) == 3 
    assert calculator.devide(6,0) == False
