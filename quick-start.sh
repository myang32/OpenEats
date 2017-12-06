#!/usr/bin/env sh

echo "OpenEats quick setup script"

echo "Downloading docker-compose.yml"
wget https://github.com/RyanNoelk/OpenEats/blob/master/docker-prod.yml

echo "Take some backups"
https://github.com/RyanNoelk/OpenEats/blob/master/docker-prod.yml

echo "Downloading Images"
docker pull openeats/api
docker pull openeats/node
docker pull openeats/nginx

echo "Starting OpenEats"
docker-compose stop
docker-compose -f docker-prod.yml up -d

echo "Sleeping for 15 seconds, then testing"
sleep 15
if [[ $? -eq "1" ]]; then
   curl -vvvv http://127.0.0.1/api/v1
   echo ""
   echo "If the above curl command was a success then you're all set!"
else
   echo "Something failed, please check and see what it was."
   exit 1
fi
exit 0