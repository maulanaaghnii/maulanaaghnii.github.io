# Docker

Docker is an open platform for developing, shipping, and running applications. Docker enables you to separate your applications from your infrastructure so you can deliver software quickly. With Docker, you can manage your infrastructure in the same ways you manage your applications. By taking advantage of Docker's methodologies for shipping, testing, and deploying code, you can significantly reduce the delay between writing code and running it in production.

## Show All Images

```
docker images
```

## Show Container

```
docker ps
```

show all container both active & inactive
```
docker ps -a
```

## Build
```
docker build -t <image_name>:<tag_version> .
```
## Run Container

```
docker run -d --name container_name <image_name>:<tag_version>
```
with port mapping
```
docker run -d -p <host_port>:<container_port> --name container_name <image_name>:<tag_version>
```

## Stop Container

```
docker stop CONTAINER_ID
```

## Start Container
```
docker start CONTAINER_ID
```

## Restart Container

```
docker restart CONTAINER_NAME_OR_ID
```

## Delete Image

```
docker rmi IMAGE_ID
```

with force method

```
docker rmi -f IMAGE_ID
```

## Delete Container

```
docker rm CONTAINER_ID
```

with force method
```
docker rm -f CONTAINER_ID
```