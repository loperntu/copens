#-*-coding:utf8-*-
from urllib import urlopen
from bs4 import BeautifulSoup
from codecs import open
def get_page(url):
	try:
		page=urlopen(url).read().decode('utf8')
		f=open('chinese.txt','a','utf8')
		for line in BeautifulSoup(page).get_text().split():
			if line[0]>u'一':f.write(line+'\n')
		f.close()
		return page,1
	except:return '',0
def get_next_target(page):
	start_link=page.find('<a href=')
	if start_link==-1:return None,0
	start_quote=page.find('"',start_link)
	end_quote=page.find('"',start_quote+1)
	url=page[start_quote+1:end_quote]
	return url,end_quote
def get_all_links(page):
	links=[]
	while 1:
		url,end_quote=get_next_target(page)
		if url:
			if url[:4]=='http' and url.find('tw')>0:links.append(url.strip('/'))
			page=page[end_quote:]
		else:break
	return links
def crawl_web():
	tocrawl=[url.strip() for url in open('tocrawl.url','r','utf8')]
	crawled=[url.strip() for url in open('crawled.url','r','utf8')]
	print tocrawl
	print crawled
	while tocrawl:
		link=tocrawl.pop()
		if link not in crawled:
#			print link
	#		if len(crawled)>9:break
			page,chinese=get_page(link)
			tocrawl+=get_all_links(page)
			crawled+=[link]
			if chinese:break

	c=open('crawled.url','w','utf8')
	for link in crawled:c.write(link+'\n')
	c.close()

	t=open('tocrawl.url','w','utf8')
	for link in tocrawl:
		print link
		t.write(link+'\n')
	t.close()

crawl_web()
