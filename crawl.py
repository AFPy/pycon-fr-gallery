#!/usr/bin/env python3

import requests
import json

with open('db.json') as db:
    db = json.load(db)
for line in db:
    with open(line["key"], "wb") as imgfile:
        imgfile.write(requests.get(f"http://paullaroid.pycon.fr/pyconfr-2106/{line['key']}/raw/").content)
