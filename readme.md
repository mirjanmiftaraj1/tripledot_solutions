### We can deploy ML House Pricing using uvicorn and python

#### Code that makes it possible:
```bash
uvicorn app.server:app --reload

python /app/client.py
```

### Or we can deploy ML House Pricing model with FastAPI, Docker, and Heroku

#### Create Docker and run the container with the following commands:

```bash
docker build -t app-name .

docker run -p 80:80 app-name
```



