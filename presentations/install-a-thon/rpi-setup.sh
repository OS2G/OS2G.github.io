#!/bin/bash

# ==[ DESCRIPTION ]============================================================
#
# this script downloads UNL's wifi setup script and runs it, connecting you to
# eduroam
#
# the script will prompt you for your username and password

# ==[ COMMANDS USED ]==========================================================
#
#   sudo
#     means "super user does..." and is what you prefix a command with if you
#     want to run it with admin permissions (like for installing things)
#
#   apt
#     means "aptitude" and is the name of the program you use to download new
#     programs.  "sudo apt install PROGRAM_NAME" installs PROGRAM_NAME,
#     "sudo apt update" makes sure you are up-to-date, and
#     "apt search SOMETHING" searchs for a program named SOMETHING
#
#   mkdir
#     means "make directory".  creates a new folder with a name
#
#   cd
#     means "change directory".  moves you into a folder
#
#   wget
#     means "web get" and is used to download files from the internet
#
#   bash
#     "bash" is what runs commands like "sudo", "apt", and "mkdir".  if you
#     run "bash FILE" then it will be as if you typed out everything in FILE
#     directly into the command prompt

# ==[ PROGRAM ]================================================================

# install the library python3-dbus, which UNL's script needs
sudo apt install python3-dbus

# create and enter downloads folder
mkdir downloads
cd downloads

# download UNL's eduroam wifi script
wget --post-data 'request=deployLinux' --out-document 'eduroam-setup.sh' https://cloud.securew2.com/public/25806/nu-net/php/deploy.php

# run the UNL script you just downloaded
bash eduroam-setup.sh
