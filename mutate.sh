#!/bin/bash

source servervars.sh
echo "Mutating Code"
ssh -i ~/.ssh/babylon_rsa -p $PORT $USER@$HOST "sed -i -s 's/)_-_PROJECT_NAME_-_(/${NAME}/g' /var/www/$NAME/core/index.py" >/dev/null
echo "Updating Permissions"
ssh -i ~/.ssh/babylon_rsa -p $PORT $USER@$HOST "sudo chown -R $WEBUSER:$WEBUSER /var/www" >/dev/null
