#!/usr/bin/env python

import sys, csv

answers = {
    8 : {
        "I have never programmed." : 0,
        'I program less than one a year.' : 1,
        "I program several times a year." : 2,
        "I program once a month." : 3,
        "I program once a week or more." : 4
    },
    10 : {
        'I could not complete this task.' : 0,
        'I could complete the task with documentation or search engine help.' : 1,
        'I could complete the task with little or no documentation or search engine help.' : 2
    },
    11 : {
        'I am not familiar with Git.' : 0,
        'I am familiar only with the name Git.' : 1,
        'I am familiar with Git but have never used it.' : 2,
        'I am familiar with Git because I have used or am using it.' : 3
    },
    13 : {
        'I am not familiar with\xc2\xa0unit testing or code coverage.' : 0,
        'I am familiar only with the terms "unit testing" and "code coverage".' : 1,
        'I am familiar with\xc2\xa0unit testing or code coverage\xc2\xa0but have never used it.' : 2
    },
    17 : {
        'I am not familiar with\xc2\xa0the command line.' : 0,
        'I am familiar only with the\xc2\xa0term "command line".' : 1,
        'I am familiar with\xc2\xa0the command line\xc2\xa0but have never used it.' : 2,
        'I am familiar with\xc2\xa0the command line\xc2\xa0because I have used or am using it.' : 3
    }
}

reader = csv.reader(sys.stdin)

try:
    for j, row in enumerate( reader ):
        if j == 0: continue
        total = 0
        for i in answers:
            total += answers[i][row[i].strip()]
        print total, row[1], row[2]

except IndexError, e:
    print >> sys.stderr, 'INDEX', row, '::', i
except KeyError, e:
    print >> sys.stderr, 'KEY', e, row, '::', answers[i].keys()
