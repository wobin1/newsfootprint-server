From python:3.12-slim

# set working directory
WORKDIR /app


# set environment variables for optimize python 
ENV PYTHONDONTWRITEBYTECODE = 1
ENV PYTHONUNBUFFERED = 1


# Copy requirements.txt to working directory
COPY requirements.txt requirements.txt


# install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt


# exposing application port
EXPOSE 8000


# make entry file executable
# RUN chmod +x /app/entrypoint.prod.sh

# start application using gunicorn
CMD ["python", "reefs_news/manage.py", "runserver", "0.0.0.0:8000"]

