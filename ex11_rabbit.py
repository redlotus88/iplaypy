#!/usr/bin/env python
# -*- coding: UTF-8 -*-

a1 = 1
b2 = 1

for i in range(1, 21):
	print'%12ld %12ld' % (a1, b2),
	if (i % 3) == 0:
		print ''
	a1 = a1 + b2
	b2 = a1 + b2
