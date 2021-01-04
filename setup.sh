#!/bin/bash

if [ "$EUID" -ne 0 ]
then
	echo -e "\e[91m[-]\e[0m Error: Permission Denied"
	echo -e "\e[93m[!]\e[0m Action: Run as root or with sudo"
	exit
fi

apt update
apt install python3-pip
pip3 install -r requirements.txt
mkdir -p /usr/share/shellclip/shells/
cp -r revshells/ /usr/share/shellclip/shells/
cp shellclip.py /usr/bin/shellclip