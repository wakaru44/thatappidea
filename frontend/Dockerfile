FROM nginx:latest

# TODO: The official nginx dockerfile probably has some specifiq env vars

ENV nginx_home=/var/www

RUN mkdir -p /var/www/thisapp

WORKDIR /var/www/thisapp

ADD . .

# And now some sort of supervisord or nginx service must go up
