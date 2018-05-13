#!/bin/bash
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
sudo cp object_request_photobooth.service /lib/systemd/system
systemctl enable object_request_photobooth.service
