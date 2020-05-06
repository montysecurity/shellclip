#!/usr/bin/python3

import pyperclip, requests, re

shells_url = str("https://github.com/montysecurity/literature/find/master")

r = requests.get(shells_url)
body = str(r.text)
matches = re.findall("notes/persistence/shells/reverse.", body)

print(body)
print(matches)
