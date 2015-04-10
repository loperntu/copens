a={
'0':{'H':.8,'C':.2},
'H':{'H':.7,'C':.3},
'C':{'H':.4,'C':.6}
}

b={
'H':{'1':.2,'2':.4,'3':.4},
'C':{'1':.5,'2':.4,'3':.1}
}

def FORWARD(o=[None,'3','1','3']):
	forward=dict()

	# initialization
	forward['H']={1:a['0']['H']*b['H'][o[1]]}
	forward['C']={1:a['0']['C']*b['C'][o[1]]}

	# recursion
	for t in range(2,3):
		for s in ['H','C']:
			forward[s][t]=0
	#	forward[s][2]=forward['H'][1]*a['H'][s]*b[s]['1']+forward['C'][1]*a['C'][s]*b[s]['1']
			for s_prime in ['H','C']:
				forward[s][t]+=forward[s_prime][t-1]*a[s_prime][s]*b[s][o[t]]
#		forward['C'][2]=forward['H'][1]*a['H']['C']*b['C']['1']+forward['C'][1]*a['C']['C']*b['C']['1']
	return forward

print FORWARD()
