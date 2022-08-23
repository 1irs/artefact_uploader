FROM python:3.10-slim

COPY pipe.py /
COPY requirements/base.txt /requirements/
RUN pip install -r /requirements/base.txt

ENTRYPOINT ["python3", "pipe.py"]
