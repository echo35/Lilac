# Lilac
A custom-built website backend in mod_python

## Installation
##### Note
These instructions assume you are configuring a Debian based machine. If you run another distro like CentOS or Arch, some of the files and commands used will vary.

##### Requirements
 - Apache2
 - mod_python
 - rsync on both host + client

##### Setup
Add this to `/etc/apache2/apache2.conf`
```
DocumentRoot "/var/www/lilac/core"
<Directory "/var/www/lilac/core">
    Options FollowSymLinks
    AllowOverride None
    Require all granted
    AddHandler mod_python .py
    PythonHandler mod_python.publisher
    PythonDebug On
    DirectoryIndex index.py
</Directory>
```

Create a file `/etc/apache2/sites-available/lilac.conf`:
```
NameVirtualHost *:80
<VirtualHost *:80>
    ServerAdmin youremail@yourdomain.tld
	DocumentRoot /var/www/lilac/core/
</VirtualHost>
```

Clone this repository to any machine with bash installed (compatible with Bash for Windows 10).
Make sure `./servervars.sh` is properly configured:
```
HOST="192.168.56.2"                 # Server IP
PORT=22                             # Server SSH port (for uploading)
USER="user"                         # SSH login
NAME="lilac"                        # Project name, determines directory path (e.g. /var/www/lilac)
WEBUSER="www-data"                  # Apache2 user, for setting access permissions
SSH_PARAMS="-i ~/.ssh/custom_id"    # Put extra SSH command options here, such as identity files
```

Once this information is corrected, go ahead and run `./install.sh`:
```
$ ./install.sh
Before proceeding, please ensure that Apache has been configured with mod_python, that servervars.sh has been set, and that rsync is installed on both the remote host and this machine.
Continue? [y/N]: y
Creating Remote Directories
Syncing lilac core (core app)
Syncing lilac data (misc data)
Syncing lilac hidden (hidden data)
Pulling logs
Mutating Code
Updating Permissions
$
```

After this, be sure to `# a2ensite lilac` and `# service apache2 reload`. Navigate to your server's IP and:
![Screenshot](https://i.gyazo.com/5c38d00236f0ceb5cb800c82489183ba.png)

Congratulations, you got it working!
