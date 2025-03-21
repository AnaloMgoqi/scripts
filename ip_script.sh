#!/bin/bash

# This script checks and prints your public IP address

# Use curl to fetch the public IP address from an external service.
public_ip=$(curl -s https://ifconfig.me)

# Check if curl succeeded in fetching the IP address.
if [ $? -ne 0 ] || [ -z "$public_ip" ]; then
    echo "Error: Unable to retrieve public IP."
    exit 1
fi

echo "Your public IP address is: $public_ip"
