FROM python:3.9
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
RUN mkdir /app/data && echo "[]" > /app/data/users.json
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]