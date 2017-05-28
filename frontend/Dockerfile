FROM nginx:alpine
# see https://hub.docker.com/_/nginx/

ENV nginx_home=/usr/share/nginx/html

COPY .  /usr/share/nginx/html

WORKDIR /usr/share/nginx/html

# And now some sort of supervisord or nginx service must go up
