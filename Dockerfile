FROM python:3.7-slim

# Set up application directory
ENV APP /app
WORKDIR $APP

# Move application contents
COPY app $APP
COPY README.md $APP

# Install dependencies
RUN pip install -r $APP/requirements.txt

CMD exec gunicorn --bind :$PORT --workers 5 --threads 8 app:app
