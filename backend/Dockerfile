FROM alpine:latest

RUN mkdir -p /opt/thisapp

WORKDIR /opt/thisapp

ADD . .

RUN virtualenv env && \
    source env/bin/activate && \
    pip install -r requirements.txt

EXPOSE 5000


CMD ["/usr/bin/python","app.py"]
