FROM rubiklabs/mkdocs:latest AS builder
WORKDIR /app
COPY . .
RUN mkdocs build
FROM scratch AS export-stage
COPY --from=builder /app/site/ .