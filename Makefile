all:
	python fretboard.py 

dropd:
	python fretboard.py -t "Drop D"

pep:
	flake8 fretboard.py

test:
	pytest test_fretboard.py

help:
	python fretboard.py --help

.PHONY: dropd pop test help
