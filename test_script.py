# test_script.py
from script import sum_xy

def test_sum_xy():
    assert sum_xy(2, 3) == 5
    assert sum_xy(-1, 1) == 0