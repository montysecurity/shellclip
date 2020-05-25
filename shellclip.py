#!/usr/bin/python3

import pyperclip
import argparse
import sys
import os

parser = argparse.ArgumentParser(description="Copy Reverse Shell Code Straight to Clipboard for Many Languages")
parser.add_argument('-l', '--list', action='store_true', help="list payloads available")
parser.add_argument('--lhost', type=str, help="the machine to callback to")
parser.add_argument('--lport', type=str, help="the port to callback to")
parser.add_argument('-c', '--code', type=str, help="the language the reverse shell should be written in")

if len(sys.argv) == 1:
	parser.print_help(sys.stderr)
	sys.exit(1)

args = parser.parse_args()
lhost = args.lhost
lport = args.lport
lang = str(args.code)
list_payloads = args.list

if list_payloads == True:
	os.system("ls revshells/ | tr ' ' '\n' | tr [:lower:] [:upper:] | awk -F. '{print $2}'")
	exit()

syscall = str("cat shells/*." + lang + " | sed 's/0.0.0.0/" + str(lhost) + "/g' | sed 's/5253/" + str(lport) + "/g' ")
pyperclip.copy(os.popen(syscall).read())
