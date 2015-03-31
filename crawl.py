#-*-coding:utf8-*-
from urllib import urlopen
def get_page(url):
	try:
		output=''
		page=urlopen(url).read().decode('utf8')
		for c in page:
			if c>=u'一':output+=c
		print output
		return page
	except:return ''
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
def crawl_web(seed):
	tocrawl=[seed]
	crawled=[]
	while tocrawl:
		link=tocrawl.pop()
		if link not in crawled:
			print link
			crawled+=[link]
			if len(crawled)>9:break
			tocrawl+=get_all_links(get_page(link))
			crawled+=[link]
	return crawled
crawl_web('http://tw.yahoo.com')
