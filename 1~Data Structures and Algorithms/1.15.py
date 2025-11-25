"""
U have a sequence of dictionaries or instances and u want to iterate over the data in groups based on the value of a
particular field, such as date
"""
rows = [
    {"address": "123 Main Street", "date": "07/01/2012"},
    {"address": "45 Pine Avenue", "date": "08/15/2013"},
    {"address": "89 Lake Road", "date": "09/22/2014"},
    {"address": "10 Maple Drive", "date": "11/03/2015"},
    {"address": "77 Oak Street", "date": "12/18/2016"},
    {"address": "250 Hill View", "date": "01/29/2017"},
    {"address": "600 River Park", "date": "03/10/2018"},
    {"address": "81 Sunset Blvd", "date": "04/14/2019"},
    {"address": "5 Cedar Lane", "date": "06/25/2020"},
    {"address": "900 Forest Way", "date": "07/30/2021"}
]

from operator import itemgetter
from itertools import groupby

#Sort by the desired field first
rows.sort(key=itemgetter('date'))

#Iterate in groups
for date, items in groupby(rows, key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ', i)

