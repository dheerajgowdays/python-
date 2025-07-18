from bank1 import value

def test_value():
    assert value('Hello')==0
    assert value('hi')==20
    assert value('hey')==20
    assert value('Good Morning')==100




