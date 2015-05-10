from __future__ import division
from codecs import open

def add_to_dict(si,sj,a):
	if si not in a:a[si]={sj:1}
	elif sj not in a[si]:a[si][sj]=1
	else:a[si][sj]+=1

def train_asbc():
	for line in open('ASBC_5.0.IOB',encoding='utf8').readlines()[:3]:
		words=line.split()
		s0,(o1,s1)='0',words[0].split('/')
		add_to_dict(s0,s1,a)
		add_to_dict(s1,o1,b)
		for i in range(1,len(words)-1):
			oi,si=words[i].split('/')
			oj,sj=words[i+1].split('/')
			add_to_dict(si,sj,a)
			add_to_dict(si,oi,b)

def normalize_and_sparse(d):
	vocabulary=set()
	for s in d:
		for o in d[s]:vocabulary.add(o)
	for s in d:
		z=sum(d[s].values())
		for o in d[s]:d[s][o]/=z
		for o in vocabulary:
			if o not in d[s]:d[s][o]=0
		
a={'0':{'I':0}};b={}
train_asbc()
states=b.keys()
normalize_and_sparse(a);normalize_and_sparse(b)

def VITERBI(o=[None,'3','1','3']):
	viterbi=dict()
	backpointer=dict()
	for state in states:
		viterbi[state]={1:a['0'][state]*b[state][o[1]]}
		viterbi[state]={1:a['0'][state]*b[state][o[1]]}
		backpointer[state]={1:'0'}
	for t in range(2,len(o)):
		for s in states:
			maximum=0
			for s_prime in states:
				temp=viterbi[s_prime][t-1]*a[s_prime][s]*b[s][o[t]]
				if temp>=maximum:
					maximum=temp
					viterbi[s][t]=maximum
					backpointer[s][t]=s_prime
	result=[]
	if viterbi[u'I'][len(o)-1]>viterbi[u'B'][len(o)-1]:s=u'I'
	else:s=u'B'
	for t in range(len(o)-1,0,-1):
		result.insert(0,o[t]+'/'+s)
		s=backpointer[s][t]
	print ' '.join(result)

o=[word[0] for word in open('ASBC_5.0.IOB',encoding='utf8').readlines()[1].split()]
o.insert(0,None)
VITERBI(o=o)
