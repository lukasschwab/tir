import click, sys, os, hashlib, pytz
from xml.etree import ElementTree as ET
from datetime import datetime
from dateutil import parser

# Hacky script to reverse the rendered tir HTML.
# Be careful if you've customized tir at all.

# FIXME: change this to your html location.
html = "/Users/lukas/Desktop/programming/lukasschwab.github.io/tir.html"

path = os.path.expanduser(html)
with open(path, "r") as f:
    contents = [unicode(l, 'utf-8') for l in f.readlines()]

header_i = []
for i, s in enumerate(contents):
    if "colspan" in s: header_i += [i]
header_i += [len(contents)-1]

days = []
for x in range(0, len(header_i)-1):
    days += [contents[header_i[x]:header_i[x+1]]]

out = []
for day in reversed(days): out += day

contents[header_i[0]:header_i[-1]] = out

with open(path, "w") as f:
    contents = "".join(contents).encode('utf-8')
    f.write(contents)
