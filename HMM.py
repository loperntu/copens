a={
'0':{'H':.8,'C':.2},
'H':{'H':.7,'C':.3},
'C':{'H':.4,'C':.6},
'0':{'VB':.019,'TO':.0043,'NN':.041,'PPSS':.067},
'VB':{'VB':.0038,'TO':.0350,'NN':.047,'PPSS':.007},
'TO':{'VB':.83,'TO':0,'NN':.00047,'PPSS':0},
'NN':{'VB':.004,'TO':.016,'NN':.087,'PPSS':.0045},
'PPSS':{'VB':.23,'TO':.00079,'NN':.0012,'PPSS':.00014}
}

b={
'H':{'1':.2,'2':.4,'3':.4},
'C':{'1':.5,'2':.4,'3':.1},
'VB':{'I':0,'want':.0093,'to':0,'race':.00012},
'TO':{'I':0,'want':0,'to':.99,'race':0},
'NN':{'I':0,'want':.000054,'to':0,'race':.00057},
'PPSS':{'I':.37,'want':0,'to':0,'race':0}
}

states=['H','C']
states=['VB','TO','NN','PPSS']

def VITERBI(o=[None,'3','1','3']):
	viterbi=dict()
	backpointer=dict()
	for state in states:
		viterbi[state]={1:a['0'][state]*b[state][o[1]]}
		viterbi[state]={1:a['0'][state]*b[state][o[1]]}
		backpointer[state]={1:'0'}
	for t in range(2,5):
		for s in states:
			maximum=0
			for s_prime in states:
#				print s_prime,t-1,viterbi[s_prime][t-1]
#				print s_prime,s,a[s_prime][s]
				temp=viterbi[s_prime][t-1]*a[s_prime][s]*b[s][o[t]]
				if temp>=maximum:
					maximum=temp
					viterbi[s][t]=maximum
					backpointer[s][t]=s_prime
			print viterbi
			print backpointer

def FORWARD(o=[None,'3','1','3']):
	forward=dict()
	for state in states:forward[state]={1:a['0'][state]*b[state][o[1]]}
	for t in range(2,3):
		for s in states:
			forward[s][t]=sum([forward[s_prime][t-1]*a[s_prime][s]*b[s][o[t]] for s_prime in ['H','C']])
VITERBI(o=[None,'I','want','to','race'])
