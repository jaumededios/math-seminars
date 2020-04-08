class SeminarCrawler():
	def __init__():
		pass;


class MITACT(SeminarCrawler):
	def __init__():
		

parser = {
    'host': lambda x:x['Host'],
    'title': lambda x: x['Title'],
    'start_time' : lambda x : formatstring(x['Date'],x['Start_Time'], x['Timezone']),
    'end_time' : lambda x : formatstring(x['Date'],x['End_Time'], x['Timezone']),
    'start_time_as_date': lambda x: stringtodate(x['Date'],x['Start_Time'], x['Timezone']),
    'end_time_as_date': lambda x: stringtodate(x['Date'],x['End_Time'], x['Timezone']),
    'speaker' : lambda x: x['Speaker'],
    'speaker_inst': lambda x: x['Speaker_inst'],
    'timezone': lambda x: x['Timezone'][4:10].replace(':',''),
    'talk_site': lambda x: x['Site'],
    'categories': lambda x : '' if (not isinstance(x['arXiv'],str) or str(x['arXiv']).lstrip().rstrip() =='') \
                                else '"'+'","'.join(x['arXiv'].upper().replace(' ','').replace('MATH.','').split(','))+'"',
    'abstract': lambda x: x['Abstract'],
    'name': lambda x: 'talk/'+(x['Host']+'_'+x['Speaker'].replace(' ','_')+'_'+x['Date']).replace('/','')+'.md'
}