FROM python

WORKDIR /usr/src/app
COPY . .
RUN pip install django pillow

EXPOSE 8000
RUN python manage.py runserver 0.0.0.0:8000
