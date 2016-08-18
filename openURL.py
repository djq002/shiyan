#coding-utf8
import urllib2
url = 'http://www.baidu.com'
req = urllib2.request(url)
response = urllib2.urlopen(req)
print response.read()
