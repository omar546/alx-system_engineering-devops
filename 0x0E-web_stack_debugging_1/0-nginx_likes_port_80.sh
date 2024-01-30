#!/bin/bash
# Check Nginx configuration
nginx_config="/etc/nginx/nginx.conf"
if [ ! -f "$nginx_config" ]; then
    echo "Nginx configuration file not found: $nginx_config"
    exit 1
fi

# Update Nginx configuration to listen on port 80
sed -i 's/listen\s*80;/listen 80 default_server;/g' "$nginx_config"

# Restart Nginx service
service nginx restart
