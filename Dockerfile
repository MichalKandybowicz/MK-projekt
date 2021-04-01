# Pull base image
FROM python:3.8

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install dependencies

COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

#COPY Pipfile Pipfile.lock /code/
#RUN pip install pipenv && pipenv install --system
