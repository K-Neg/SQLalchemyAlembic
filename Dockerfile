# Pull base image
FROM python:3.7

# Set environment varibles
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt


COPY ./source /app
COPY .env /app

EXPOSE 5000

CMD ["python","main.py"]