#!/bin/bash

# My shell script to install jenkins
#-qq No output except for errors

echo "Updating apt-get"
sudo apt-get -y -qq update

echo "Installing java jdk 11"
sudo apt install openjdk-11-jdk -y > /dev/null 2>&1

echo "Adding Jenkins repo"
wget -q -O - https://pkg.jenkins.io/debian/jenkins.io.key | sudo apt-key add -
echo deb http://pkg.jenkins.io/debian-stable binary/ | sudo tee /etc/apt/sources.list.d/jenkins.list

echo "Updating apt-get"
sudo apt-get -y -qq update

echo "Installing git"
sudo apt-get -y install git > /dev/null 2>&1

echo "Installing jenkins"
sudo apt-get -y install jenkins > /dev/null 2>&1
sudo systemctl start jenkins
sudo systemctl enable jenkins


sleep 1m

echo "Url"
IP=$(ip -br addr  show |grep 192|egrep -o '([0-9]{1,3}\.){3}[0-9]{1,3}')
echo "http://"$IP":8080/"

echo "Password for first start"
JENKINSPWD=$(sudo cat /var/lib/jenkins/secrets/initialAdminPassword)
echo $JENKINSPWD
