FROM python:3.8-slim
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV FLASK_APP=flaskr:create_app
EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]