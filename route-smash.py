#!/usr/bin/env python

## routesmash.py - 29/07/2014
## ben.dale@gmail.com
## Spam a list of generated /24 prefixes 
## Use with ExaBGP for load testing

import sys
import time

for first in range(1,223):
	for second in range(0,255):
		for third in range(0,255):
			sys.stdout.write('announce route %d.%d.%d.0/24 next-hop 10.0.0.31\n' % (first, second, third))
			sys.stdout.flush()
			##time.sleep(0.001)

while True:
	time.sleep(1)
