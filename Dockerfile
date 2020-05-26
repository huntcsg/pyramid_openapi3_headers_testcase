FROM python:3.7.5

WORKDIR /code
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./
EXPOSE 6543
CMD ["python", "app.py"]
