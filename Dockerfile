FROM python:3.10-slim

COPY pipe.py pipe.py
COPY requirements/base.txt requirements/base.txt
RUN pip install -r requirements/base.txt

ENTRYPOINT ["python3", "pipe.py"]
