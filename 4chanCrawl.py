#!/home/jonkman666/bin/python
import MySQLdb
import math
import string
import bs4
import urllib2
from urlparse import urlparse

emma = ["petite","feet","gluten","shrill","annoying","stompy","cutie",
		"publications","kitties","stampy","nervous","self-deprecating","insecure",
		"A-cup","snickers","grumpy","anal","breakable", "white","gaydrunk","smart",
		"opinionated","cooldrunk","tapeworm","compact", "emma","valley","cuba","irate","pouty","bitchface",
		"toilet", "books", "journalism", "rhode", "coffee", "adderall", "wine", "whiskey", "sister", "bangs", 
		"fringe", "lotr", "lord", "hobbit", "frump", "bolano", "roberto", "lipstick","baltimore", "bobbing", "apples", "beyonce"
		"chat","pale","white"]
#single words describing emma. this should be more kind. i'm no thesaurus
fourChan = ["/a/","/b/","/c/", "/d/", "/e/", "/f/", "/g/","/h/","/i/","/int/","/ic/","/k/","/hr/","/m/","/o/","/p/","/r/","/s/","/t/","/u/","/v/","/vr/","/vg/","/w/","/wg/",
			"/r9k/","/gif/","/s4s/","/cm/","/hm/","/lgbt/", "/y/", "/3/", "/adv/","/an/","/asp/","/cgl/","/ck/" ,"/co/","/diy/" , "/fa/", "/fit/", "/gd/", "/hc/","/jp/",
			 "/lit/", "/mlp/", "/mu/", "/n/","/out/", "/po/", "/pol/", "/sci/", "/soc/","/sp/", "/tg/" ,"/toy/", "/trv/", "/tv/", "/vp/","/wsg/","/x/"]
#all 4chan boards
fourChanCollect = {}
#array of dictionaries which == all boards
for board in fourChan:	
	thisBoard = {}
	#dictionary of this board
	#start loop
	URL = "http://boards.4chan.org" + board
	#build string based on board
	req = urllib2.Request(URL)
	try:
	    resp = urllib2.urlopen(req)
	except urllib2.URLError, e:
	    if e.code == 404:
	    	break
	html_doc = urllib2.urlopen(URL)
	from bs4 import BeautifulSoup
	soup = BeautifulSoup(html_doc)
	threads = soup.findAll('div',{'class':'thread'})
	#find all threads
	pageLength = len(threads)
	#length of threads
	x = 0
	#make a fucking sweet integer fuck.
	while x < pageLength:
		threadTitle = threads[x].contents[0].contents[0].find_all('span',{'class':'subject'})
		bodyText = threads[x].contents[0].blockquote
		bodyText = str(bodyText)
		threadTitle = threadTitle[0].string
		#search and stringify
		for adj in emma:
			if threadTitle != None and bodyText != None:
				#so long as it's not null...
				size = len(threadTitle)
				threadTitle = threadTitle[0:size]
				threadTitle = threadTitle.lower()
				#make lowercase for find
				titleResult = threadTitle.find(adj)
				bodyResult = bodyText.find(adj)
				#figure out if emma is in title of thread
				if titleResult >= 0 or bodyResult >= 0:
					#if ya. put link in final thing.
					print "yes found it: " + threadTitle
					link = threads[x].contents[0].contents[0].find_all('a',{'class':'replylink'})
					link = URL + link[0]['href']
					#aw cute a match. make a keyvalue
					thisBoard[threadTitle]=link
					try:
						db = MySQLdb.connect(host="xxxxxx",user="xxxxxxx",passwd="xxxxxxxx",db="xxxxxxxx") 
						cur = db.cursor()
						print "gonna insert"
						cur.execute("INSERT INTO crawl(url, title, body, exist, board, datetime) VALUES(%s, %s, %s, 1, %s, CURRENT_TIMESTAMP);",(link,threadTitle,bodyText,board,))
						cur.close()
						db.close()
						print "that went through"
					except MySQLdb.Error, e:
						print "Error %d: %s" % (e.args[0],e.args[1])
						continue
		x = x +1 #end this page
	fourChanCollect[board]=thisBoard
print "\nso happy it's over thank you for touching all of 4chan!\n"	