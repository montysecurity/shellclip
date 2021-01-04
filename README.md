# shellclip
Copy Reverse Shell Code Straight to Clipboard for Many Languages

## setup
	
	git clone https://github.com/montysecurity/shellclip.git
	cd shellclip/
	bash setup.sh

## usage

```
$ shellclip 
usage: shellclip [-h] [-l] [--lhost LHOST] [--lport LPORT] [-c CODE]

Copy Reverse Shell Code Straight to Clipboard for Many Languages

optional arguments:
  -h, --help            show this help message and exit
  -l, --list            list payloads available
  --lhost LHOST         the machine to callback to
  --lport LPORT         the port to callback to
  -c CODE, --code CODE  the language the reverse shell should be written in
```

## languages supported
- Bash
- C
- Perl
- PHP
- PowerShell (PS1)
- Python
