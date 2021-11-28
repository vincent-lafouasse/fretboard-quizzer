#!/usr/bin/env python

import numpy as np
import argparse
from rich.console import Console
from rich import inspect
from rich.traceback import install

install(show_locals=True)


def main():
    console = Console()
    tuning, difficulty = parse_arguments()
    courses = {number: note for number, note in zip(range(1, 7), tuning)}

    while 1:
        note, string = random_note_and_string(tuning, difficulty)
        # print(note, string)
        print(f"Where can u fret {NOTES[note]} on string {string}")
        answer = int(input())
        correction = (answer + courses[string]) % 12 == note
        console.print(
            ":thumbsup: [bold blue]Yes !![/bold blue]"
            if correction
            else ":thumbsdown: [bold magenta]No...[/bold magenta]"
        )


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


def parse_arguments():
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
    tuning = args.tuning
    tunings_dict = {
        "E standard": (4, 11, 7, 2, 9, 4,),
        "Drop D": (4, 11, 7, 2, 9, 2,),
    }
    difficulty = args.difficulty
    difficulties_dict = {
        "easy": (0, 6),
        "medium": (0, 8),
        "hard": (0, 10),
        "full": (0, 12),
    }
    return (tunings_dict[tuning], difficulties_dict[difficulty])


def random_note_and_string(tuning, difficulty):
    minimum, maximum = difficulty
    course_number = np.random.randint(1, 7)
    fret_to_play = np.random.randint(minimum, maximum)
    return ((fret_to_play + tuning[course_number - 1]) % 12, course_number)


if __name__ == "__main__":
    main()
