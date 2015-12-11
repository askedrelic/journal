.PHONY: all
all: env install

env:
	virtualenv env

install:
	pip install -r requirements.txt

test:
	tox

clean:
	find . -name '*.pyc' -delete
	find . -name '__pycache__' | xargs rm -rf
