from urllib import urlopen
url1='http://xkcd.com/353'
url2='http://xkcd.com/554'
def get_page(url):
	#if url in [url1,url2]:
	return urlopen(url).read()
	return ''
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
			if url[:4]=='http':links.append(url.strip('/'))
			page=page[end_quote:]
		else:break
	return links
def crawl_web(seed):
	tocrawl=[seed]
	crawled=[]
	while tocrawl:
		link=tocrawl.pop()
		if link not in crawled:
			tocrawl+=get_all_links(get_page(link))
			crawled+=[link]
		if len(crawled)>9:break
	return crawled

for link in crawl_web('http://tw.yahoo.com'):
	print link
