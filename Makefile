help:
	@echo "That App idea Main Repo Tools";
	@echo "";
	@echo "todos     - Print the TO DO lines in the whole repo";
	@echo "build     - Build whole project, API and Frontend";
	@echo "run-dev   - Run the dev environment with compose";
	@echo "deploy    - Deploy Instructions for API and Frontend";
	@echo "frontend  - Do something about the frontend";
	@echo "backend   - Do something about the backend ";

todos:
	find .  -maxdepth 3 -type f   \( ! -path "*vendor*" \) \( ! -path "*.git*" \)  -exec grep -H "TODO:" --color=always  {} \;

build: tools/docker-compose.yml backend/Dockerfile frontend/Dockerfile
	@docker-compose -f tools/docker-compose.yml build

run-dev: build
	@docker-compose -f tools/docker-compose.yml up -d

deploy:
	@echo"TODO: Some instructions to run the ansible that deploys this shit";
frontend:
	@echo "TODO: add makefile command to run the frontend container";

backend:
	@echo "TODO: add makefile command to run the backend container";
