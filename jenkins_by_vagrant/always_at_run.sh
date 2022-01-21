#!/bin/bash

echo "Url"
IP=$(ip -br addr  show |grep 192|egrep -o '([0-9]{1,3}\.){3}[0-9]{1,3}')
echo "http://"$IP":8080/"
