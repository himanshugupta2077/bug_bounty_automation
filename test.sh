#!/bin/bash

echo -e "go to vm setting and enable shared folder and check auto-mount option"

mkdir ~/shared
sudo mount -t vboxsf vm_shared_dir /home/{finduser}/shared