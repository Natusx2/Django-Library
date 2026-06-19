FROM python:3.14.3-slim

WORKDIR /code

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py migrate
RUN python manage.py loaddata books

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
