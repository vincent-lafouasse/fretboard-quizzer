import pytest
from rich import inspect
import fretboard as fret

# Quiz class

def test_easy_setting():
    quiz = fret.Quiz('easy')
    assert quiz.frets == (0, 6)

def test_hard_setting():
    quiz = fret.Quiz('hard')
    assert quiz.frets == (0, 10)

def test_invalid_setting():
    with pytest.raises(AssertionError) as exc_info:
        quiz = fret.Quiz('why am i here i play the trombone')

# Guitar class
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

def test_default_tuning():
    guitar = fret.Guitar()
    assert tuple(guitar.strings.values()) == (4, 11, 7, 2, 9, 4,)

def test_string_dict():
    guitar = fret.Guitar()
    expected = {1: 4,
            2: 11,
            3: 7,
            4: 2,
            5: 9,
            6: 4,}
    assert guitar.strings == expected

if __name__ == '__main__':
    test_invalid_tuning()
