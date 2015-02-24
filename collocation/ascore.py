#-coding:utf-8-*-
from __future__ import division
#from __future__ import print_function
from json import load
from math import log
d=load(open('../triples.json',encoding='utf-8'))

def w1_R_s(w1,R):
    sum=0
    for w2 in d[w1][R]:
        sum+=d[w1][R][w2]
    return sum

def s_s_w2(w2):
    sum=0
    for w in d:
        for R in d[w]:
            if w2 in d[w][R]:
                sum+=d[w][R][w2]
    return sum

def w2_s_s(w2):
    sum=0
    if w2 in d:
        for r in d[w2]:
            for c in d[w2][r]:
                sum+=d[w2][r][c]
    return sum

def w1_R_w2(w1,R,w2):
    return d[w1][R][w2]

def Dice(A,R,B):
    fAB=w1_R_w2(A,R,B)
    fA=w1_R_s(A,R)
    fB=w2_s_s(B)
    return 2*fAB/(fA+fB)

def AS(w1,R,w2):
    return 14+log(Dice(w1,R,w2),2)

def ASi(w):
    sum=0
    for r in d[w]:
        for c in d[w][r]:
            sum+=AS(w,r,c)
    return sum

def sort_by_freq(w,r):
    return sorted(d[w][r].items(),key=lambda x:x[1],reverse=True)

def sort_by_dice(w,r):
    a=dict()
    cs=d[w][r].keys()
    for c in list(cs):
        a[c]=Dice(w,r,c)
    return sorted(a.items(),key=lambda x:x[1],reverse=True)

def Dist(w1,w2):
    numerator=0
    for r in d[w1]:
        if r in d[w2]:
#    r='nsubj'
            for c in d[w1][r]:
                if c in d[w2][r]:
                    AS1,AS2=AS(w1,r,c),AS(w2,r,c)
                    numerator+=AS1+AS2-(AS1-AS2)**2/50
    denominator=ASi(w1)+ASi(w2)
    return numerator/denominator

if __name__=='__main__':
    res=dict()
    words=[u'樂',u'愉快',u'愉',u'有趣',u'美好']
    words+=[u'經常',u'時常',u'勤',u'常常',u'常',u'恆']
    words+=[u'原因',u'關係',u'肇始',u'因',u'故',u'導因',u'緣']
    words+=[u'按照',u'按',u'依照',u'依據',u'根據']
    words+=[u'相當',u'很',u'相當於',u'具體',u'莫大',u'重大',u'重要',u'直接']
#    for w in d.keys()[:44]:
 #       res[w]=Dist(u'快樂',w)
  #  for word,dist in sorted(res.items(),key=lambda x:x[1],reverse=True):
   #     print(word.encode('utf-8'),dist)
#    for c,freq in sort_by_dice(u'快樂','nsubj'):
#        print c.encode('utf-8'),freq
