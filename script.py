"""
high level support for doing this and that.
"""
import os
import codecs
from collections import defaultdict
import requests
from lxml.html.diff import htmldiff

"""
Test changes to web platforms.
This script will send the same request to two different servers and compares
the status codes, response times and diff the html.
Get access logs from your  running servers.
Parse them to get the  urls.
Define an url prefix for each environment.
"""

# Getting variables from the environment.
OLD_NODE = os.environ(['OLD_NODE'])
NEW_NODE = os.environ(['NEW_NODE'])
FILE_NAME = os.environ(['URL_FILE'])

# Open the log and get urls.
with codecs.open(FILE_NAME, "r", encoding='utf-8', errors='ignore') as f:
    CONTENT = f.readlines()

# Send request to each version and print main performance counter and file path.
for url in CONTENT:
    print(url)
    f = requests.get(NEW_NODE + url)
    g = requests.get(OLD_NODE + url)
    h = defaultdict()
    i = defaultdict()
    h = f.text
    i = g.text
    if f.status_code != g.status_code:
        print('http status code diference!!!')
    print("new", f.status_code, "old", g.status_code, '/n',
          "history-new", f.history, '/n', "history-old", g.history)
    print(htmldiff(f.text, g.text))
