#! /usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime as dt
import os

print("Content-type:text/plain\r\n\r\n")
now = dt.now()
print(now)
print(os.environ)
print(os.environ['QUERY_STRING'])
print(os.environ['REQUEST_METHOD'])
print()

path = os.environ['PATH_INFO']

if path == "/foo":
    print("foo"*100)
elif path == "/bar":
    print("bar"*30)
elif path == "/news":
    print(os.environ['QUERY_STRING'])
else:
    print("error")


def get_foo():
    print("foo"*100)

def get_bar():
    print("bar"*30)

# routes = {
#     '/foo': get_foo,
#     '/bar': get_bar
# }


