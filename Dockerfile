FROM python:3.10

ADD ./birthday/main.py .

COPY ./birthday/reqirements.txt .

RUN pip install -r requirements.txt

COPY ./birthday ./birthday

CMD ["main.py", "./birthday/main.py"]