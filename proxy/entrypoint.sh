#!/bin/sh
cat /etc/nginx/http.conf.template | envsubst '$HTTP_SERVER_PORT' > /etc/nginx/conf.d/http.conf
exec nginx -g "daemon off;"