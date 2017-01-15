#!/bin/bash

source servervars.sh
echo "Pulling logs"
rsync -e "ssh -p $PORT $SSH_PARAMS" -qazr --delete --progress $USER@$HOST:"/var/www/${NAME}/logs/" logs
