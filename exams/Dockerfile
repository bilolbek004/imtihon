FROM python:3.11-alpine
WORKDIR /ap
ENV TOKEN=default_token_value
COPY requirement.txt /ap/
COPY exam.py /ap/
RUN pip install -r requirement.txt
ENTRYPOINT ["python","exam.py"]