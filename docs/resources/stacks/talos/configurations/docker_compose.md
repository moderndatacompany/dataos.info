# `docker_compose.yaml` configurations

Docker compose manifest file is used to configure the docker image of Talos. This section will describe each attribute to help you configure the docker-compose manifest file.

```yaml
version: "2.2"
services:
  pg-db:
    build: ./database
    container_name: employee-db
    environment:
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: 12345
    ports:
      - "54321:5432"
    networks:
      - app-network
    healthcheck:
      test: [ "CMD-SHELL", "pg_isready -U postgres" ]
      interval: 10s
      timeout: 5s
      retries: 5

  talos:
    image: rubiklabs/talos:0.1.6
    ports:
      - "3000:3000"
    volumes:
      - .:/etc/dataos/work
    environment:
      DATAOS_RUN_AS_USER: iamgroot
      DATAOS_RUN_AS_APIKEY: bG9jYWNsLmE1YWE3MGM1LTA5MGIfgdfhf56788hggFmLTY1NzMxODVlMThiNA==
      DATAOS_FQDN: https://liberal-donkey.dataos.app
    tty: true
    depends_on:
      pg-db:
        condition: service_healthy
    networks:
      - app-network
      
networks:
  app-network:
    driver: bridge
```

### `version`

**Description:** Specifies the version of the Docker Compose file format.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Valid semantic version format, e.g., "2.2", "3.7" |

**Example Usage:**

```yaml
version: "2.2"
```

---

### `services`

**Description:** Defines the services (containers) that will be part of this Docker Compose configuration.

---

### `pg-db`

**Description:** Configuration for the PostgreSQL database service.

### `build`

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | Path to the build context for the image |

**Example Usage:**

```yaml
build: ./database
```

---

### `container_name`

**Description:** Custom name for the container. This is useful for easier identification and management of the container.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | none | Custom name for the container |

**Example Usage:**

```yaml
container_name: employee-db
```

---

### `environment`

**Description:** Key-value pairs for environment variables that will be set inside the container.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| map | optional | none | Key-value pairs for environment variables |

**Example Usage:**

```yaml
environment:
  POSTGRES_USER: postgres
  POSTGRES_PASSWORD: 12345
```

---

### `ports`

**Description:** List of port mappings between the host and the container. It specifies which ports on the host will be forwarded to ports on the container.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of port mappings (host) |

**Example Usage:**

```yaml
ports:
  - "54321:5432"
```

---

### `networks`

**Description:** List of networks the service is connected to. This defines which Docker networks the service will use.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of networks the service is connected to |

**Example Usage:**

```yaml
networks:
  - app-network
```

---

### `healthcheck`

**Description:** Configuration for health checks on the service. It includes the test command, the interval between checks, the timeout for each check, and the number of retries before marking the service as unhealthy.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| map | optional | none | Health check configuration (test, interval, timeout, retries) |

**Example Usage:**

```yaml
healthcheck:
  test: [ "CMD-SHELL", "pg_isready -U postgres" ]
  interval: 10s
  timeout: 5s
  retries: 5
```

---

### `talos`

**Description:** Configuration for the Talos service.

---

### `image`

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | mandatory | none | Docker image name and tag |

**Example Usage:**

```yaml
image: rubiklabs/talos:0.1.6
```

---

### `ports`

**Description:** List of port mappings between the host and the container. It specifies which ports on the host will be forwarded to ports on the container.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of port mappings (host) |

**Example Usage:**

```yaml
ports:
  - "3000:3000"
```

---

### `volumes`

**Description:** List of volume mounts between the host and the container. It specifies which directories or files on the host will be mounted into the container.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of volume mounts (host) |

**Example Usage:**

```yaml
volumes:
  - .:/etc/dataos/work
```

---

### `environment`

**Description:** Key-value pairs for environment variables that will be set inside the container.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| map | optional | none | Key-value pairs for environment variables |

**Example Usage:**

```yaml
environment:
  DATAOS_RUN_AS_USER: iamgroot
  DATAOS_RUN_AS_APIKEY: bG9jYWNsLmE1YWE3MGM1LTA5MmLTY1NzMxODVlMThiNA==
  DATAOS_FQDN: https://liberal-donkey.dataos.a
```

---

### `tty`

**Description:** Allocate a TTY for the container. This is useful for interactive processes and debugging.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| boolean | optional | false | true or false |

**Example Usage:**

```yaml
tty: true
```

---

### `depends_on`

**Description:** Dependency configuration for service startup order. It ensures that the specified service is available and healthy before starting the dependent service.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| map | optional | none | Dependency configuration for service startup order |

**Example Usage:**

```yaml
depends_on:
  pg-db:
    condition: service_health
```

---

### `networks`

**Description:** List of networks the service is connected to. This defines which Docker networks the service will use.

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| list of strings | optional | none | List of networks the service is connected to |

**Example Usage:**

```yaml
networks:
  - app-network
```

---

### `app-network`

**Description:** Configuration for a network used by the services.

---

### `dri`

| Data Type | Requirement | Default Value | Possible Values |
| --- | --- | --- | --- |
| string | optional | "bridge" | Network driver types, e.g., "bridge", "overlay" |

**Example Usage:**

```yaml
driver: bridge
```

---