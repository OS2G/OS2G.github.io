#!/bin/bash

# create and enter downloads folder
mkdir downloads
cd downloads

# download UNL's eduroam wifi script
wget --post-data 'request=deployLinux' https://cloud.securew2.com/public/25806/nu-net/php/deploy.php
mv deploy.php config-eduroam.sh

# install python3-dbus, which UNL's script needs
sudo apt install python3-dbus

# run the UNL script
bash config-eduroam.sh
