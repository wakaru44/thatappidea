FROM alpine:latest

RUN mkdir -p /opt/thisapp

WORKDIR /opt/thisapp

ADD . .

RUN apk update && apk add python && \
    apk add py-virtualenv && \
    virtualenv dev && \
    source dev/bin/activate && \
    pip install -r requirements.txt && \
    echo "|          VirtualEnv Ready             |"
    

EXPOSE 5000

# To activate teh debugger.
ENV FLASK_DEBUG=1

CMD ["dev/bin/python","app.py", "--host=0.0.0.0"]
