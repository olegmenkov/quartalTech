run:
	docker-compose build && docker-compose up -d

dump:
	psql -U user db -f ./dumps/quartal_tech.dump
