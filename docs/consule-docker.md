```
docker run -d --name=dev-consul \
  -p 8500:8500 \
  -p 8600:8600/udp \
  consul:1.15.4 agent -dev -ui -client=0.0.0.0

```