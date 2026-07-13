FROM nginx:alpine

COPY proxy/nginx.template /etc/nginx/nginx.template

COPY proxy/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
