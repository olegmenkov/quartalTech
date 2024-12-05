run:
	docker-compose build && docker-compose up -d

dump:
	docker exec db psql -U user db -f /dumps/quartal_tech.dump
