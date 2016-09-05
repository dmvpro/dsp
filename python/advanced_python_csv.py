import csv
import urllib2

# import csv file from url
reader = csv.reader(urllib2.urlopen('https://raw.githubusercontent.com/dmvpro/dsp/master/python/faculty.csv'))

next(reader) #skip header

emails = [row[3] for row in reader] # extract column 4 from data
             
with open("emails.csv", "wb") as f:  # create export file
    writer = csv.writer(f,delimiter="\n")  # write csv delimited by new lines
    writer.writerows([emails])  # export file
