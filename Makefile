GIT_COMMIT=$(shell git rev-parse HEAD || echo '?')
GIT_TREE=$(shell git diff-index --quiet HEAD -- && echo clean || echo dirty)
GIT_TAG=$(shell git describe --tags --abbrev=0)
GIT_VERSION=$(shell git describe --tags --dirty || echo dev-$(shell date -u +"%Y%m%d%H%M%S"))
BUILD_DATE=$(shell date -u +"%Y-%m-%dT%H:%M:%SZ")

DOCKER_IMAGE_PREFIX=rubiklabs
DOCKER_IMAGE=dataos-docs
DOCKER_TAG=$(GIT_VERSION)

mkdocs-remove:
	docker image rm rubiklabs/mkdocs:latest
mkdocs-build:
	docker build -t rubiklabs/mkdocs:latest -f ./docker/Dockerfile.mkdocs .
mkdocs-push:
	docker push rubiklabs/mkdocs:latest

setup:
	docker run --rm -it -p 8000:8000 -v '$(shell PWD)':/docs rubiklabs/mkdocs:latest new .
serve:
	docker run --rm -it -p 8000:8000 -v '$(shell PWD)':/docs rubiklabs/mkdocs:latest
build:
	mkdir -p site && \
	docker build \
	--progress auto \
	--output site \
	-t ${DOCKER_IMAGE_PREFIX}/${DOCKER_IMAGE}:${DOCKER_TAG} \
	-f ./docker/Dockerfile . 

.release:
	echo "Creating release with => $(CMD) ..."
	docker run --rm -it \
  -v "`pwd`:/home/build/working_dir" \
  -v ~/.gitconfig:/home/build/.gitconfig \
  -v ~/.ssh:/home/build/.ssh \
  rubiklabs/builder:0.2.0 \
  $(CMD)

release-dev-major: CMD=dev major
release-dev-major: .release

release-dev-minor: CMD=dev minor
release-dev-minor: .release

release-dev-patch: CMD=dev patch
release-dev-patch: .release

release-dev-none: CMD=dev none
release-dev-none: .release

release-public-major: CMD=public major
release-public-major: .release

release-public-minor: CMD=public minor
release-public-minor: .release

release-public-patch: CMD=public patch
release-public-patch: .release

release-public-none: CMD=public none
release-public-none: .release