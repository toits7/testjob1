FROM nginx:alpine

COPY nginx.template /etc/nginx/nginx.template

COPY entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
