# Build MkDocs site
FROM rubiklabs/mkdocs:latest AS mkdocs
WORKDIR /app
COPY . .
RUN mkdocs build

# Build DataOS server
FROM node:12.16.1-alpine AS server
ENV NODE_ENV=production
ARG GIT_VERSION
ARG BUILD_DATE
RUN apk add --update --no-cache \
   python python-dev py-pip make g++ perl git \
   build-base openssh-client openssh-server tree \
   && pip install virtualenv \
   && rm -rf /var/cache/apk/*

# KEYS
RUN mkdir -p /root/.ssh && \
    chmod 0700 /root/.ssh && \
    ssh-keyscan bitbucket.org > /root/.ssh/known_hosts
COPY .keys/bitbucket-readonly /root/.ssh/id_rsa 
COPY .keys/bitbucket-readonly.pub /root/.ssh/id_rsa.pub
RUN  chmod 600 /root/.ssh/id_rsa /root/.ssh/id_rsa.pub

WORKDIR /app
COPY . . 
RUN npm ci --prefix server
WORKDIR /app/server
# Copy static files from mkdocs
COPY --from=mkdocs /app/site/ /app/server/public
RUN echo "GIT_VERSION=$GIT_VERSION" > public/release.txt && \
    echo "BUILD_DATE=$BUILD_DATE" >> public/release.txt
RUN npm prune --production


# Final
FROM node:12.16.1-alpine

WORKDIR /usr/app
COPY --from=server /app/server .
COPY ./docker/docker-entrypoint /docker-entrypoint
RUN cat public/release.txt

ENV NODE_ENV production
ENV APP__PORT 8000
EXPOSE 8000
ENTRYPOINT ["/docker-entrypoint"]

RUN ["chmod", "+x", "/docker-entrypoint"]
WORKDIR /usr/app