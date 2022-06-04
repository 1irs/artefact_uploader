FROM python:3.10-slim

COPY pipe.py requirements.txt /
RUN pip install -r requirements.txt

ENTRYPOINT ["python3", "pipe.py"]
