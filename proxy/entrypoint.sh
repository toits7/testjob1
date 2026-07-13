#!/bin/sh
envsubst < /etc/nginx/nginx.template > /etc/nginx/conf.d/template.conf
exec nginx -g "daemon off;"