import pandas as pd
import datetime as dt
import numpy as np

def stringtodate(date, time, timezone):
    string = date+' '+time+timezone[4:10].replace(':','')
    return dt.datetime.strptime(string,"%d/%m/%Y %H:%M:%S%z")

def formatstring(date, time, timezone):
    date = stringtodate(date,time,timezone)
    return dt.datetime.strftime(date,"%Y-%m-%dT%H:%M:%S"+timezone[4:10])

data = pd.read_csv('data.csv')

base_string = \
'''+++
  host= "{host}"
  date = "{start_time}"
  expiryDate = "{end_time}"
  title = "{title}"
  speaker = "{speaker}"
  speaker_institution = "{speaker_inst}"
  talk_site = "{talk_site}"
  categories = [{categories}]

  publishDate = "2000-02-07T16:00:00-07:00"
+++

{abstract}'''

parser = {
    'host': lambda x:x['Host'],
    'title': lambda x: x['Title'],
    'start_time' : lambda x : formatstring(x['Date'],x['Start_Time'], x['Timezone']),
    'end_time' : lambda x : formatstring(x['Date'],x['End_Time'], x['Timezone']),
    'speaker' : lambda x: x['Speaker'],
    'speaker_inst': lambda x: x['Speaker_inst'],
    'talk_site': lambda x: x['Site'],
    'categories': lambda x : '' if (not isinstance(x['arXiv'],str) or str(x['arXiv']).lstrip().rstrip() =='') \
                                else '"'+'","'.join(x['arXiv'].upper().replace(' ','').replace('MATH.','').split(','))+'"',
    'abstract': lambda x: x['Abstract'],
    'name': lambda x: 'talk/'+(x['Host']+'_'+x['Speaker'].replace(' ','_')+'_'+x['Date']).replace('/','')+'.md'
}

for row in data.iterrows():
    mydict = { prop:func(row[1]) for prop, func in parser.items()}

    with open(mydict['name'], 'w') as f:
        f.write(base_string.format(**mydict))