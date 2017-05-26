help:
	@echo "That App idea Main Repo Tools";
	@echo "";
	@echo "todos     - Print the TO DO lines in the whole repo";
	@echo "deploy    - Deploy Instructions for API and Frontend";
	@echo "frontend  - Do something about the frontend";

todos:
	find .  -maxdepth 3 -type f   \( ! -path "*vendor*" \) \( ! -path "*.git*" \)  -exec grep -H "TODO:" --color=always  {} \;

deploy:
	@echo "TODO: add makefile command to deploy the whole stack";

frontend:
	@echo "TODO: add makefile command to run the frontend container";

backend:
	@echo "TODO: add makefile command to run the backend container";
