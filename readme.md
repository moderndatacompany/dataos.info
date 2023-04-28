# Material for Modern Data Fabric

## Setup
_Ensure that you have [`Docker`](https://docs.docker.com/get-docker/) installed and you have logged in to Docker Hub with TMDC credentials. Contact <suraj@tmdc.io> for help._

```sh
# setup the project, needs to be done only once!
$ make setup
```

```sh
# start serving
$ make serve
```

Open [http://127.0.0.1:8000](http://127.0.0.1:8000) in your browser to access the documentation site. Do check [Tutotials](http://127.0.0.1:8000/tutotials/writing/) before you start writing content.


## Build
```
make build
```

## Test
```
export VERSION=v0.2.0-7-gf319ea9
make test
```

> Open: http://127.0.0.1:8000/docs/auth/oidc

## Publish
```
$ make push
```

## Learning Materials
### Markdown
- [The Markdown Guide](https://www.markdownguide.org/)
- [Mastering Markdown (3 minute read)](https://guides.github.com/features/mastering-markdown/)

### MkDocs
- [Project documentation with Markdown](https://www.mkdocs.org/)
- [A Material Design theme for MkDocs](https://github.com/squidfunk/mkdocs-material)
- [A Mermaid graphs plugin for mkdocs](https://github.com/fralau/mkdocs-mermaid2-plugin)

### Diagrams
- [Mermaid](https://mermaid-js.github.io/mermaid/#/)