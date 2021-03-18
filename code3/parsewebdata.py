import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE



url = 'http://py4e-data.dr-chuck.net/comments_1173076.xml'
print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)

data = uh.read()
print('Retrieved', len(data), 'characters')
#print(data.decode())

tree = ET.fromstring(data)
counts = tree.findall('.//count')
acc = 0

for count in counts:
    acc += int(count.text)

print('Count: ',len(counts))
print('Sum: ', acc)
#lat = results.find('comments').find('comment').find('count').text

#print('lat', lat)

#http://py4e-data.dr-chuck.net/comment_42.html
'''

print(results.find('commentinfo').find('comments').find('comment').find('count').text)


'''