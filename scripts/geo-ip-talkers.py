#!/usr/bin/env python
from collections import defaultdict
import GeoIP
gi = GeoIP.new(GeoIP.GEOIP_MEMORY_CACHE)
countries = defaultdict(int)
countriesoutf = open('top-talkers-brazil-contries','w+')
datafile = open('top-talkers-new-york.txt', 'r')
for line in datafile:
	myfield = line.split()
	geocountry = gi.country_code_by_addr(myfield[0])
	if geocountry is None:
		print myfield[0], myfield[1]
	else:
		countries[geocountry] += int(myfield[1])

print "Countries db has", len(countries), " entries in it"
for key, value in sorted(countries.iteritems(), key=lambda (k,v): (v,k)):
	print key, "=>", value
#	answer = (key , value)
#	s = str(value)
#	countries.write(s)
#	print myfield[1]

