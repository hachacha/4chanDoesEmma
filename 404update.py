#!/home/jonkman666/bin/python
import MySQLdb
import urllib2
import string

print "begin cleanup"
db = MySQLdb.connect(host="xxxxxx",user="xxxxxxx",passwd="xxxxxxxx",db="xxxxxxxx") 
cur = db.cursor()
cur.execute("SELECT url FROM crawl WHERE exist=1;")
rows = cur.fetchall()
cur.close()
db.close()
for i in rows:
	url= i[0]
	req = urllib2.Request(url)
	try:
		resp = urllib2.urlopen(req)
	except urllib2.URLError, e:
		if e.code == 404:
			db = MySQLdb.connect(host="xxxxxx",user="xxxxxxx",passwd="xxxxxxxx",db="xxxxxxxx") 
			cur=db.cursor()
			cur.execute("UPDATE crawl SET exist = 0 WHERE url=%s;",(url,))
			cur.close()
			db.close()
		else:
			break
print "all done with 404 cleanup"
