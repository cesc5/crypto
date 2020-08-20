# Crypto World

## build image && run container

```bash
docker build --tag crypto:latest .
docker run -tid -p 8000:8000 --name crypto crypto:latest
```

## Development

```bash
docker run -tid -p 8000:8000 --name crypto -v $(pwd):/app crypto:latest
docker logs crypto -f
```
