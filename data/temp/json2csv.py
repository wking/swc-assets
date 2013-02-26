import sys
import json

raw = {}
first = None
for filename in sys.argv[1:]:
    country, suffix = filename.split('.')
    if first is None:
        first = country
    with open(filename, 'r') as reader:
        data = json.load(reader)
    raw[country] = data

for country in raw:
    assert len(raw[country]) == len(raw[first]), \
           'Data length mismatch: {0} vs. {1}' % (country, first)

years = [x['year'] for x in raw[first]]
years.sort()

countries = raw.keys()
countries.sort()
print 'YEAR,' + ','.join(countries)

for (i, y) in enumerate(years):
    sys.stdout.write(str(y))
    for c in countries:
        sys.stdout.write(',' + str(raw[c][i]['data']))
    sys.stdout.write('\n')
