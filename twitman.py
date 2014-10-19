from msched import on_event, Insert, Any
from TwitterAPI import TwitterAPI

con_key = 'AxlDQPaU5ZzSL1P8dkfXexkIc'
con_sec = 's1lEhwMdGPzpNizzjrno0VRvw6rzWGDesFvQK7VJPpRUusfbhF'
acc_key = '2817236999-abAyCU29KrDXEhzyQPVCu60h8TLwmXEZbMR647U'
acc_sec = 'Syp1e2ygInEtRQQMbI9ZTIzkED3NCYVfr2mnKAHPhDTQC'

api = TwitterAPI(con_key,con_sec,acc_key,acc_sec)

@on_event(Insert({}))
def tweet_about(**doc):
	url = 'http://gatechffs.com/listing?listId='+doc['_id']
	desc = doc['desc']
	if len(desc) > (140-22):
		desc = desc[:140-28]+'...'
	print 'tweeting:',desc
	api.request('statuses/update', {'status':desc + ' ' + url})
