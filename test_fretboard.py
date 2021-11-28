import pytest
from rich import inspect
import fretboard as fret

# Tuning
def test_E_standard():
    assert fret.set_tuning('E standard') == (4, 11, 7, 2, 9, 4,)

def test_drop_D():
    assert fret.set_tuning('Drop D') == (4, 11, 7, 2, 9, 2,)

def test_invalid_tuning():
    tuning = (1,)
    # inspect(tuning)
    try:
        tuning = fret.set_tuning('420')
    except AssertionError:
        tuning = None
    # inspect(tuning)
    # inspect(tuning is None)
    assert tuning is None


if __name__ == '__main__':
    test_invalid_tuning()
