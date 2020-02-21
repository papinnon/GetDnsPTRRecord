fi = open('./Domains','r')

dic={}
for lines in fi:
    dic[lines[:lines.find(" ")]]   = lines[lines.find(":")+2:-2]

print(dic)
input()
f2 = open('./us_out','r')
l=[]
for lines in f2:
    ipidx= lines.find("'ip'")
    if(ipidx == -1):
        l.append(lines)
        continue
    substr = lines[ipidx+7:]
    ip = substr[:substr.find(':')]
    try:    
        tmp = dic[ip]

#####################3
        if (-1!=tmp.find('ailed')):
            l.append(lines)
            continue
########################
        tmp = lines[:-2]+'('+tmp+'),\n'
        l.append(tmp)
    except Exception as e:
        #print (e)
        l.append(lines)
        continue

f3 = open('./newusout','w')
for i in l:
    f3.write(i)
