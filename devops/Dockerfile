FROM python:3.7
RUN apt-get update -y
RUN apt-get install -y python-pip python-dev build-essential netcat-openbsd

COPY src /source
COPY tests /tests
COPY setup.cfg /
COPY conftest.py /
COPY devops/entrypoint.sh /

WORKDIR /

COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

RUN chmod +x /entrypoint.sh
CMD ["/bin/bash", "/entrypoint.sh"]
