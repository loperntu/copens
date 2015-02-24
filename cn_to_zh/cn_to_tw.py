from codecs import open
from jieba import cut

d=dict()

def cn_to_tw():
    for line in open('cn_to_tw_phrase.csv',encoding='utf8'):
        cn,zh=line.strip().split(',')
        d[cn]=zh
    for line in open('b2g_map.utf8',encoding='utf8'):
        b=line.strip().split(u' ')[0]
        g=line.strip().split(u' ')[1]
        d[g]=b
    return d

cn_to_tw()

text=open('cn.txt',encoding='utf8').read()
for word in cut(text):
    if word in d:print d[word],
    else:
        for c in word:
            if c in d:print d[c],
            else:print c,
