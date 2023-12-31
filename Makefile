manage_py := sudo docker compose exec -it backend python app/manage.py

run:
	$(manage_py) runserver

migrate:
	$(manage_py) migrate

makemigrations:
	$(manage_py) makemigrations

shell:
	$(manage_py) shell_plus --print-sql

celery:
	cd app && celery -A settings worker -l INFO --autoscale=0,10

beat:
	cd app && celery -A settings beat -l INFO

pytest:
	pytest ./app/tests --cov=app --cov-report html && coverage report --fail-under=75

collectstatic:
	$(manage_py) collectstatic --no-input && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static