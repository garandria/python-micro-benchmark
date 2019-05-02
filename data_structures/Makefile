
docker:
	rm -f *~
	rm -rf __pycache__
	docker build -t pythonds .
	docker tag pythonds aaronspirals/pythonds
	docker push aaronspirals/pythonds
