
setup:
	docker run --rm -it -p 8000:8000 -v '$(shell PWD)':/docs rubiklabs/mkdocs:latest new .
serve:
	docker run --rm -it -p 8000:8000 -v '$(shell PWD)':/docs rubiklabs/mkdocs:latest
build:
	rm -rf site/ && \
	mkdir -p site && \
	docker build \
	--progress auto \
	--output site \
	-t rubiklabs/ddp-website:latest \
	-f ./Dockerfile . 
