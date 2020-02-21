import json
f = open("./shodan-export.json",'r')
def printj(jso):
    print("{")
    try:
        print("'ip': '{:<}',".format(jso["ip_str"]+':'+str(jso['port'])))
        print("'org': '{:<}',".format(jso['org']))
    except Exception as e:
        pass
    if (len(jso['hostnames']) != 0 and jso['hostnames'][0].find('no-rev')==-1):
        print("'hostnames': '{:<}',".format(jso['hostnames'][0]))
    else:
        pass
    #print(jso['location'])
    try:
        sub = jso['ssl']['cert']['subject']
    except Exception as e:
        print('}')

    for key in ['CN','L','O','OU','ST','emailAddress']:
        try:
            print("'"+key+"'"+": '{:<}'".format(sub[key]))
        except:
            continue

    print("}")


#dict_keys(['_shodan', 'hash', 'os', 'opts', 'ip', 'isp', 'http', 'port', 'ssl', 'hostnames', 'location', 'timestamp', 'domains', 'org', 'data', 'asn', 'transport', 'ip_str'])
#for i in f:
#    js = json.loads(i)
#    ssl = js['ssl']
#    cert = ssl['cert']
#    sub = cert['subject']
#    print(sub.keys())
#    for k in sub.keys():
#        print(sub[k])
#        input()

for lin in f:
    jsn = json.loads(lin)
    printj(jsn)


