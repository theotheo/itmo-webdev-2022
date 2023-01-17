#! /usr/bin/env python

from datetime import datetime as dt

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Python-generated Page</title>')
print('</head>')
print('<body>')
now = dt.now()
print(f'<h2>{now}</h2>')
print('</body>')
print('</html>')