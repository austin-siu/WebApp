FROM ubuntu:16.04

RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /Desktop/app/requirements.txt

WORKDIR /Desktop/app

RUN pip install -r requirements.txt

COPY . /Desktop/app

ENTRYPOINT [ "python" ]

CMD [ "localserver.py" ]