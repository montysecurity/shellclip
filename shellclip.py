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
lang = args.code
list_payloads = args.list

def build_languages():
	languages = []
	for root, dirs, files in os.walk("/usr/share/shellclip/shells/revshells/", topdown=False):
		for name in files:
			languages.append(str(name.split(".")[1]))
	return languages

def list_languages():
	languages = build_languages()
	for lang in languages:
		print(lang)
	exit()

if list_payloads == True:
	list_languages()

if lhost == None:
	print(str("[-] Error: No LHOST Specified"))
	print(str("[!] Action: Use \"--lhost\" Option"))
	exit()
elif lport == None:
	print(str("[-] Error: No LPORT Specified"))
	print(str("[!] Action: Use \"--lport\" Option"))
	exit()
elif lang == None:
	print(str("[-] Error: No Language Specified"))
	print(str("[!] Action: Use \"--code\" or \"-c\" Option"))
	exit()
else:
	languages = build_languages()
	if lang not in languages:
		print("[-] Error: Language not supported")
		print("[!] Action: Use one of the following languages")
		list_languages()
	else:
		syscall = str("cat /usr/share/shellclip/shells/revshells/*." + lang + " | sed 's/0.0.0.0/" + str(lhost) + "/g' | sed 's/5253/" + str(lport) + "/g' ")
		pyperclip.copy(os.popen(syscall).read())