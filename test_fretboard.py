import pytest
from rich import inspect
import fretboard as fret

# Tuning
def test_E_standard():
    guitar = fret.Guitar('E standard')
    assert tuple(guitar.strings.values()) == (4, 11, 7, 2, 9, 4,)


def test_drop_D():
    guitar = fret.Guitar('Drop D')
    assert tuple(guitar.strings.values()) == (4, 11, 7, 2, 9, 2,)


def test_invalid_tuning():
    with pytest.raises(AssertionError) as exc_info:
        guitar = fret.Guitar('420')

def test_retune():
    guitar = fret.Guitar('E standard')
    assert tuple(guitar.strings.values()) == (4, 11, 7, 2, 9, 4,)
    guitar.set_tuning('Drop D')
    assert tuple(guitar.strings.values()) == (4, 11, 7, 2, 9, 2,)


if __name__ == '__main__':
    test_invalid_tuning()
