#!/bin/sh
envsubst < /etc/nginx/nginx.template > /etc/nginx/conf.d/default.conf
exec nginx -g "daemon off;"