FROM python:3.8

WORKDIR /code
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY bot bot
COPY core core
COPY goals goals
COPY todolist todolist
COPY manage.py .
COPY README.md .

CMD python manage.py runserver 0.0.0.0:8000
