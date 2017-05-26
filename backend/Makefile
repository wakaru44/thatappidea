# A simple makefile to make things simpler

help:
	@echo "This App™. This API";
	@echo "";
	@echo "help           - This text";
	@echo "todo           - Will print all the TODO's in the code";
	@echo "dev            - Run the dev server";
	@echo "setup          - Setup the virtualenv";
	@echo "";


todo:
	grep  -r "TODO:" * --exclude-dir ENV --exclude Makefile

dev:
	python app.py

setup:
	virtualenv env; source env/bin/activate && pip install -r requirements.txt

docker-build: Dockerfile
	@docker build . -t thisapi

docker-run: docker-build
	@docker run -ti thisapi:latest /bin/sh
