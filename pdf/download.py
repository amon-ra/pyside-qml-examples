# -*- coding: utf-8 -*-

import urllib2

def filename(x):
    return x.strip().replace(' ', '_')

for line in open('articles.txt'):
    if not line.strip():
        continue
    url = 'http://developer.qt.nokia.com/wiki/pdf/%s' % filename(line)
    file = filename(line)+'.pdf'
    print file, '...',
    d = urllib2.urlopen(url).read()
    f = open(file, 'wb')
    f.write(d)
    f.close()
    print 'OK'

