from pymongo import MongoClient

client = MongoClient(host='localhost', port=27017)
#client.PTT.authenticate('username','password')
res = client.PTT.Gossiping.find()

for post in res:
    for key in [u'post_time', u'author', u'URL', u'ip', u'boo_num', u'arrow_num', u'push_num', u'comments', u'content', u'comment_differenceValue', u'title', u'content_seg', u'_id']:print key,post[key]
