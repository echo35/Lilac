#!/bin/bash

source servervars.sh
ssh $SSH_PARAMS -p $PORT $USER@$HOST "sudo chown -R $USER:$WEBUSER /var/www" >/dev/null
echo "Syncing ${NAME} core (core app)"
rsync -e "ssh -p $PORT $SSH_PARAMS" -qazr --delete --progress core/ $USER@$HOST:"/var/www/${NAME}/core/"
echo "Syncing ${NAME} data (misc data)"
rsync -e "ssh -p $PORT $SSH_PARAMS" -qazr --delete --progress data/ $USER@$HOST:"/var/www/${NAME}/data"
echo "Syncing ${NAME} hidden (hidden data)"
rsync -e "ssh -p $PORT $SSH_PARAMS" -qazr --delete --progress hidden/ $USER@$HOST:"/var/www/${NAME}/hidden/"
