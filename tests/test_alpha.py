import sys, os
sys.path.append(os.getcwd())

from src.simpleUID import alpha
from utils import has_upper, has_lower
import os


def test_default():
    generated = alpha()
    assert len(generated) == 6

def test_uppercase():
    generated = alpha(case="upper")
    assert has_upper(generated) == True
    assert has_lower(generated) == False

def test_lowercase():
    generated = alpha(case="lower")
    assert has_upper(generated) == False
    assert has_lower(generated) == True

def test_prefix():
    generated = alpha(prefix="abc")
    assert len(generated) == 9
    assert generated[:3] == "abc"
    
def test_length():
    generated = alpha(200)
    assert len(generated) == 200
