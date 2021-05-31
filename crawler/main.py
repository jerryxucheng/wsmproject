import urllib.request
import re
txts=[]
file = open("alltxt.txt")
while 1:
    line = file.readline()
    line=line.strip("\n")
    txts.append(line)
    if not line:
        break
file.close()
url = txts[200001]
request = urllib.request.Request(url)
request.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
response = urllib.request.urlopen(request)
response.encoding = ('utf-8')
buf = response.read()
buf = str(buf, encoding='utf-8',errors='ignore')
print(str(url))
filename=url[27:]
f=filename.replace("/","-")
file=open("./data"+"/"+f,"a+")
buf = buf.encode('gbk', 'ignore')
buf = buf.decode('gbk', 'ignore')
file.write(buf)
file.close()


for i in range(175644  ,200000):
    url=txts[i]
    request = urllib.request.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36')
    response = urllib.request.urlopen(request)
    buf = response.read()
    buf = str(buf, encoding='utf-8',errors='ignore')
    filename=url[27:]
    f=filename.replace("/", "-")
    file=open("./data"+"/"+f, "a+",)
    buf=buf.encode('gbk','ignore')
    buf=buf.decode('gbk','ignore')
    file.write(buf)
    file.close()
    print(i)