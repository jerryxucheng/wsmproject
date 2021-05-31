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

for i in range(300000 , 600000):
    url=txts[i]
    filename = url[27:]
    f = filename.replace("/", "-")
    file1 = open('C:/Users/11746/Desktop/data2/data'+'/'+f, 'r')
    Lines = file1.readlines()
    file2 = open('./processed'+'/'+f, 'a+')
    for line in Lines:
        if line[8] != '<' or line[0] != '[':
            continue
        index1=line.find(']')
        time=line[1:index1]
        index2=line.find('<')
        index3=line.find('>')
        speaker=line[index2+1:index3]
        blank1=line.find(' ',index3+1)
        blank2=line.find(' ',blank1+1)
        blank3 = line.find(' ', blank2 + 1)
        colon=line.find(':',blank1)
        receiver=''
        if colon>0 and colon<blank3:
            receiver=line[blank1+1:colon]
        else:
            receiver=' '
        if receiver!=' ':
            content=line[colon+2:]
        else:
            content=line[index3+2:]
        file2.write("time: "+time+" speaker: "+speaker+" receiver: "+receiver+" content: "+content)
    file1.close()
    file2.close()
    print(i)