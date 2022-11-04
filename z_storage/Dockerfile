FROM python:3.8-slim-buster

ADD ./z_storage.py /

ARG key="Genotyper/1/DNAsensor/**"

RUN pip install --upgrade pip pip install maturin pip install eclipse-zenoh
CMD python3 './z_storage.py'

