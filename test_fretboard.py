import pytest
import fretboard as fb

# Tuning
def test_E_standard():
    assert fb.set_tuning('E standard') == (4, 11, 7, 2, 9, 4,)

def test_drop_D():
    assert fb.set_tuning('Drop D') == (4, 11, 7, 2, 9, 2,)
