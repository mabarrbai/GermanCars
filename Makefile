all: install start

test: install
	echo "Testing app model..."
	python manage.py test

start: install
	echo "Starting app..."
	python manage.py runserver

install:
	echo "Installing necessary packages..."
	pip install -r requirements.txt

doc:
	echo ""Generating HTML documentation...""	
	pydoc -w ./
		 