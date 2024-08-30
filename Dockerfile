FROM python:3.12.1

RUN pip install --upgrade pip 

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY ./app /code/app

EXPOSE 8000

#CMD ["uvicorn", "app.server:app"]
CMD ["uvicorn", "app.server:app", "--host", "127.0.0.1", "--port", "8000"]