#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import bs4
import sys

import requests

print(sys.version)

res = requests.get('http://nostarch.com')
res.raise_for_status()

noStarchSoup = bs4.BeautifulSoup(res.text)
print(type(noStarchSoup))
