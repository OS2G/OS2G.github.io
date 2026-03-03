#!/bin/bash

# install and run tailscale's install script
curl -fsSL https://tailscale.com/install.sh | sh

echo 'to start tailscale with ssh enabled, run: sudo tailscale up --ssh'
echo 'to stop tailscale, run: sudo tailscale down'
echo 'to see its status, run: tailscale status'
echo 'to enter this device while tailscale is running, go to another device (logged onto the same tailnet) and run: ssh YOUR_USERNAME_HERE@YOUR_HOSTNAME_HERE'
echo '  for instance: ssh admin@webfox'
