#!/usr/bin/env python

import numpy as np
import argparse
from rich.console import Console
from rich import inspect
from rich.traceback import install

install(show_locals=True)
console = Console()


def main():
    tuning_choice, difficulty_choice = parse_sysargs()
    guitar = Guitar(tuning_choice)
    quiz = Quiz(difficulty_choice)
    quiz.play(guitar.strings)


class Quiz:
    def __init__(self, difficulty_choice):
        self.frets = None
        self.set_frets(difficulty_choice)

    def play(self, tuning):
        while 1:
            rand_fret, rand_string = self.get_random_question()
            rand_note = (tuning[rand_string] + rand_fret) % 12
            console.print(
                f"Where can u fret {NOTES[rand_note]} on string {rand_string}",
                style="bold green",
            )
            guess = get_answer()
            if guess == 420:
                return 0
            console.print(
                ":thumbsup: [bold blue]Yes !![/bold blue]\n"
                if rand_fret % 12 == guess % 12
                else ":thumbsdown: [bold magenta]No...[/bold magenta]\n"
            )

    def set_frets(self, difficulty_choice):
        # easy mode uses only frets 0-5
        # full mode uses all frets
        difficulties_dict = {
            "easy": (0, 6),
            "medium": (0, 8),
            "hard": (0, 10),
            "full": (0, 12),
        }
        assert difficulty_choice in difficulties_dict
        self.frets = difficulties_dict[difficulty_choice]

    def get_random_question(self):
        minimum, maximum = self.frets
        rand_fret = np.random.randint(minimum, maximum)
        rand_string = np.random.randint(1, 7)
        return rand_fret, rand_string


class Guitar:
    """
    only attribute of Guitar objects is their tuning in self.strings
    stored as a dictionary with:
    keys are the index of the string (eg second string)
    values are the tuning of said string, with 0 means C, 1 means Db etc
    """

    def __init__(self, tuning_name):
        self.strings = None
        self.set_tuning(tuning_name)

    def set_tuning(self, tuning_name):
        tunings_dict = {
            "E standard": (4, 11, 7, 2, 9, 4,),
            "Drop D": (4, 11, 7, 2, 9, 2,),
        }
        assert tuning_name in tunings_dict
        self.strings = {
            str_number: str_note
            for (str_number, str_note) in enumerate(
                tunings_dict[tuning_name], 1
            )
        }


def parse_sysargs():
    """
    fetches the options for tuning and playing mode and returns them
    """
    parser = argparse.ArgumentParser(
        description="Test your knowledge of the guitar fretboard"
    )
    # Parse tuning
    parser.add_argument(
        "-t",
        "--tuning",
        # choices=['E standard'],
        help=(
            'choose tuning, e.g. "E standard" or "Drop D". '
            "Default is E standard"
        ),
        default="E standard",
    )
    # Parse difficulty
    parser.add_argument(
        "-d",
        "--difficulty",
        help="Determines how high on the fretboard this will go",
        default="full",
    )

    args = parser.parse_args()
    return args.tuning, args.difficulty


def get_answer():
    """
    asks for answer in standard input, checks its validity and returns it
    answer == 'exit' returns a value that causes Quiz.play() to exit
    else, keep asking until answer can be cast into int and is in [[0; 24]]
    """
    while True:
        answer = input()

        if str(answer) == "exit":
            return 420

        try:
            guess = int(answer)
            pass
        except ValueError:
            console.print("bruh", style="red")
            continue
        if guess not in range(25):
            console.print("bruh", style="red")
            continue
        else:
            break

    assert isinstance(guess, int)
    assert guess in range(25)
    return guess


NOTES = (
    "C",
    "C#",
    "D",
    "Eb",
    "E",
    "F",
    "F#",
    "G",
    "Ab",
    "A",
    "Bb",
    "B",
)

if __name__ == "__main__":
    main()
