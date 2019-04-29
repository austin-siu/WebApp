FROM ubuntu:18.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /opt/

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt ./
RUN pip3 install -r requirements.txt

RUN chmod -R 666 /opt/

COPY . .

ENTRYPOINT [ "python3" ]

CMD [ "wsgi.py" ]