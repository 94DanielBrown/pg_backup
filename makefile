default: test install

install:
	pip3 install -r requirements.txt

test:
	PYTHONPATH=./src pytest

