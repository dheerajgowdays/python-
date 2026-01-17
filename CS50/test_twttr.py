#Then, in a file called test_twttr.py, implement one or more functions that collectively test your implementation of shorten thoroughly, each of whose names should begin with test_ so that you can execute your tests with:
import pytest
from twttr1 import shorten

def test_shorten():
    assert shorten("dheeraj")=='dhrj'
    assert shorten("Charan")=='Chrn'
    assert shorten("1234/.;")=='1234/.;'
    assert shorten("hArdhIk")=='hrdhk'

