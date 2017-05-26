# A simple makefile to make things simpler

help:
	@echo "This App™. This API
	@echo "";
	@echo "help           - This text";
	@echo "todo           - Will print all the TODO's in the code";
	@echo "dev            - Run the dev server";
	@echo "";


todo:
	grep  -r "TODO:" * --exclude-dir ENV --exclude Makefile

dev:
	python app.py
