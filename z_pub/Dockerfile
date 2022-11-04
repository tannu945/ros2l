FROM python:3.8-slim-buster

ADD ./z_pub.py /

ARG key="Genotyper/1/DNAsensor/1/health"
ARG value='dead'
RUN pip install --upgrade pip pip install maturin pip install eclipse-zenoh
CMD python3 './z_pub.py'

