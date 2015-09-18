FILE=tmp.prod.json
DJANGO_ADMIN_USER=admin

help:
	@echo "The following make targets are available:"
	@echo "  * sass                     - Compile sass to css"
	@echo "  * sass-watch               - Compile sass to css on changes"
	@echo "  * docker                   - Start the docker containers"
	@echo "  * docker-init              - Initialize docker containers"
	@echo "  * docker-clean             - Remove all docker containers"
	@echo "  * docker-bash              - Run a bash in web docker container"
	@echo "  * docker-data              - Load dumped data"
	@echo "  * docker-migrate           - Apply migrations to docker env"
	@echo "  * docker-makemessages      - Generate .po locale files"
	@echo "  * docker-compilemessages   - Generate .mo locale files"
	@echo "  * docker-pw                - Change django admin pw"
	@echo ""
	@echo ""
	@echo "If you're new to the project, run this to get started:"
	@echo ""
	@echo " make docker-init docker"
	@echo ""
	@echo "If you want to change any less files run this command:"
	@echo ""
	@echo " make dev-env less-watch"

sass:
	@gulp sass

sass-watch:
	@gulp sass:watch

dev-env:
	@npm i

docker:
	@docker-compose up --no-recreate

docker-clean:
	@docker-compose kill
	@docker-compose rm -f

docker-bash:
	@docker-compose run --rm web bash

docker-init:
	@docker-compose run --rm web psql -h db -U postgres < tools/docker/cache_table.sql
	@docker-compose run --rm web app/manage.py migrate
	@docker-compose run --rm web app/manage.py loaddata tools/docker/user.json

docker-data:
	@docker-compose run --rm web python app/manage.py flush --noinput
	@docker-compose run --rm web python app/manage.py loaddata /usr/src/app/${FILE}

docker-migrate:
	@docker-compose run --rm web python app/manage.py migrate

docker-makemessages:
	@docker-compose run --rm web python app/manage.py makemessages -a

docker-compilemessages:
	@docker-compose run --rm web python app/manage.py compilemessages

docker-pw:
	@docker-compose run --rm web python app/manage.py changepassword ${DJANGO_ADMIN_USER}
