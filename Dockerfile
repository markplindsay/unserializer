FROM python:2-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 5001

ENTRYPOINT ["gunicorn"]
CMD ["--config", "config.py", "application"]
