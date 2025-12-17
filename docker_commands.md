# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume
docker volume create fastapi-db 

### Create the volume
  
```bash
docker build -t shopping-server1:v1
```

### Seed the volume (via Docker Desktop)

```bash
via Docker Desktop
```

## Server 1

### Build the image

```bash
docker build -t shopping-server1:v1 .\server1\
```

### Run the container

```bash
docker run -d -p 8000:8000 --mount source=fastapi-db,targe
t=/app/db sha256:897a1fcc563c7cdaab57b83ebe8aee6c1516bb25e998c02c1b0c87fd5b2a5626
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .\server2\
```

### Run the container

```bash
docker run -d -p 8001:8000 --mount source=fastapi-db,target=/app/db sha256:ba5d581640ac31e7f4ae075c2877d6de32dcf5cf8a760ee7b3aba2a7d96c4a37
```

