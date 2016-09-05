### Q1: Degree Count & Frequency Code
import csv
import urllib2
from collections import Counter
import re

# import csv file from url
reader = csv.reader(urllib2.urlopen('https://raw.githubusercontent.com/dmvpro/dsp/master/python/faculty.csv'))

next(reader) #skip header

ldegree = [row[1] for row in reader] # extract column 2 from data

pdegree = [a.replace('.', '') for a in ldegree] # remove periods

wdegree = [b.lstrip(' ') for b in pdegree] #remove leading whitespace

#if str contains more than one degree then split into multiple strs
sdegree = []
for c in wdegree:
    sdegree.extend(c.split())

#count the amount of different degrees
print "There are " + str(len(set(sdegree))) + " different degrees in the file:"
   
for (k,v) in Counter(sdegree).items():   #output the frequency of degrees 
    print "%s appears %d times" % (k, v)


'''
# NOTE: One faculty member has no degree listed and displays as '0' in output
#    but can be excluded with a if != 0 statement.

###
#use regex to parse/strip/conform degree_str into degrees
# degrees = re.replace(sdegree, r'[^\w\s]', '')
# if degrees:
#    print format(degrees.group(0))
###
'''


### Q2: Title Count & Frequency Code
import csv
import urllib2
from collections import Counter
import re

# import csv file from url
reader = csv.reader(urllib2.urlopen('https://raw.githubusercontent.com/dmvpro/dsp/master/python/faculty.csv'))

next(reader) #skip header

ltitle = [row[2] for row in reader] # extract column 3 from data

# slice off dept text after title:
ptitle = [i[:-17] for i in ltitle]

#count the amount of different titles
print "There are " + str(len(set(ptitle))) + " different titles in the file:"
   
for (k,v) in Counter(ptitle).items():   #output the frequency of titles 
    print "%s appears %d times" % (k, v)
    

### Q3: Print list of emails
import csv
import urllib2

# import csv file from url
reader = csv.reader(urllib2.urlopen('https://raw.githubusercontent.com/dmvpro/dsp/master/python/faculty.csv'))

next(reader) #skip header

emails = [row[3] for row in reader] # extract column 4 from data

print emails


### Q4: Print list and frequency of unique domains:
import csv
import urllib2
from collections import Counter
import re

# import csv file from url
reader = csv.reader(urllib2.urlopen('https://raw.githubusercontent.com/dmvpro/dsp/master/python/faculty.csv'))

next(reader) #skip header

emails = [row[3] for row in reader] # extract column 4 from data

#extract sub-/domain from email addresses

domains = [a.split("@")[1] for a in emails]

#count the amount of different degrees
print "There are " + str(len(set(domains))) + " unique domains in the file:"
   
for (k,v) in Counter(domains).items():   #output the frequency of degrees 
    print "%s appears %d times" % (k, v)

'''
# regex?
# domains = re.search("@[\w.]+", s)
# print domains.group()
'''
