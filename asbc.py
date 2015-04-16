#-*-coding:utf8-*-
from os import listdir
from codecs import open
from re import sub

for directory in ['ASBC_A','ASBC_B']:
	for filename in listdir(directory):
		for line in open(directory+'/'+filename,encoding='utf8'):
			start_sentence=line.find('<sentence>')
			if start_sentence==-1:continue
			end_sentence=line.find('</sentence>')
			sentence=line[start_sentence+10:end_sentence]
			print sentence.encode('utf8')
			no_pos=sub(pattern='\([A-z].*?\)',repl='',string=sentence).split(u'　')
			for word in no_pos[:-1]:
				print word[0].encode('utf8')+'/B',
				for i in range(1,len(word)):
					print word[i].encode('utf8')+'/I',
			print
			
