FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD gunicorn -w 4 -b :8000 app:app
CMD [ "python", "./manage.py", "runserver", "0.0.0.0:8000"]