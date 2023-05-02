FROM rubiklabs/mkdocs:latest AS builder
WORKDIR /app
COPY . .
RUN mkdocs build

FROM scratch AS export-stage
COPY --from=builder /app/site/ .

# FROM nginx:latest
# RUN rm /etc/nginx/conf.d/default.conf
# COPY --from=builder /app/site/ /usr/share/nginx/html/
# RUN ls -la /usr/share/nginx/html/