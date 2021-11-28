MODULE=fretboard.py
LINTER=flake8
FORMATTER=black
FFLAGS=-l 79
TEST_SUITE=test_fretboard.py

all:
	python $(MODULE) 

dropd:
	python $(MODULE) -t "Drop D"

pep:
	$(FORMATTER) $(FFLAGS) $(MODULE)
	$(LINTER) $(MODULE)

test:
	pytest $(TEST_SUITE)

check:
	python -m py_compile $(MODULE)
	$(LINTER) $(MODULE)
	$(FORMATTER) $(FFLAGS) --diff $(MODULE)
	

help:
	python $(MODULE) --help

.PHONY: dropd pep test help check
