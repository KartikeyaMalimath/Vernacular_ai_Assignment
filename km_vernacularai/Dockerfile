FROM python:3.7.2
ENV PYTHONBUFFER 1
RUN mkdir /km_api_app
WORKDIR /km_api_app
COPY requirements.txt /km_api_app/
RUN pip install -r requirements.txt
COPY . /km_api_app/
EXPOSE 8000
RUN python manage.py migrate
ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8000"]