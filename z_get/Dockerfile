FROM python:3.8-slim-buster

ADD ./z_get.py /

ARG key="Genotyper/1/DNAsensor/1/health"

RUN pip install --upgrade pip pip install maturin pip install eclipse-zenoh
CMD python3 './z_get.py'

