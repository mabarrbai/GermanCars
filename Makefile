all: install

test: install
	echo "Testing app model..."
	python manage.py test

install:
	echo "Installing necessary packages..."
	pip install -r requirements.txt

doc:
	echo ""Generating HTML documentation...""	
	pydoc -w ./
		 