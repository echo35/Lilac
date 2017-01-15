#!/bin/bash

echo "Before proceeding, please ensure that Apache has been configured with mod_python, that servervars.sh has been set, and that rsync is installed on both the remote host and this machine."

read -r -p "Continue? [y/N]: " CONFIRMATION
if [[ ! $CONFIRMATION =~ ^[Yy]$ ]]; then
	exit
fi

source servervars.sh
echo "Creating Remote Directories"
ssh -p $PORT $SSH_PARAMS $USER@$HOST "sudo sh -c 'mkdir -p /var/www/${NAME}/logs/ ; touch /var/www/${NAME}/logs/site_access.log;'" 
./update.sh
