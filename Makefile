
# .PHONY: base
# .PHONY: dev
# .PHONY: tests
# .PHONY: build



PYTHON-VERSION := 3.12
# OUTDIR := --outdir /path



ifeq ($(OS),Windows_NT)
	PYTHON-SYS = py -$(PYTHON-VERSION)
	BIN-NAME = Scripts
	EXTENSION = .exe
else
	PYTHON-SYS = python$(PYTHON-VERSION)
	BIN-NAME = bin
endif

VENV-NAME:= .venv
BIN-DIR:= $(VENV-NAME)/$(BIN-NAME)

PIP-COMPILE:= $(BIN-DIR)/pip-compile$(EXTENSION)
PYTHON:= $(BIN-DIR)/python$(EXTENSION)


#

all: requirements/requirements-dev.txt

#

requirements/requirements.txt: requirements/requirements.in $(PIP-COMPILE)
	$(PYTHON) -m piptools compile -o requirements/requirements.txt requirements/requirements.in

base: requirements/requirements.txt
	$(PYTHON) -m piptools sync requirements/requirements.txt


requirements/requirements-tests.txt: requirements/requirements.txt requirements/requirements-tests.in
	$(PYTHON) -m piptools compile -o requirements/requirements-tests.txt requirements/requirements-tests.in

tests: requirements/requirements.txt
	$(PYTHON) -m pip install -e .[tests]


requirements/requirements-dev.txt: requirements/requirements-tests.txt requirements/requirements-dev.in
	$(PYTHON) -m piptools compile -o requirements/requirements-dev.txt requirements/requirements-dev.in

dev: requirements/requirements-dev.txt
	$(PYTHON) -m pip install -e .[dev]



$(PIP-COMPILE):
	$(PYTHON-SYS) -m venv $(VENV-NAME)
	$(PYTHON) -m pip install --upgrade pip pip-tools

#

build: dev
	$(PYTHON) -m build $(OUTDIR)



