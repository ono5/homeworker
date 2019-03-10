.PHONY: test release clean all_tests ft ut mk clean flash

test:
	docker-compose build --pull release
	docker-compose build
	docker-compose run test

release:
	docker-compose up --abort-on-container-exit migrate
	docker-compose run app python3 manage.py collectstatic --no-input
	docker-compose up ${option}

all_tests:
	docker-compose run --rm app pytest

ft:
	docker-compose run --rm app pytest -v -s -l --tb=short functional_tests/${filename}

ut:
	docker-compose run --rm app pytest -v -s -l --tb=short ${dir}

mk:
	docker-compose run --rm app python3 manage.py makemigrations
	docker-compose run --rm app python3 manage.py migrate ${app_name}

clean:
	docker-compose down -v
	docker images -q -f dangling=true -f label=application=homeworker | xargs -I ARGS docker rmi -f --no-prune ARGS

flash:
	docker-compose run --rm app python3 manage.py flush --database=default --noinput
	docker-compose run --rm app python3 manage.py createsuperuser

cs:
	docker-compose run --rm app python3 manage.py collectstatic --no-input

