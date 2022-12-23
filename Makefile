DIR := ${CURDIR}
PYTHON := python
all: test run clean

test:
	${PYTHON} -m unittest
	timeout 3

run:
	${PYTHON} $(DIR)/src/main.py

clean:
	rm -rf $(DIR)/src/__pycache__
	rm -rf $(DIR)/tests/__pycache__