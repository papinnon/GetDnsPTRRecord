import requests
import socket
import urllib3
from dns import resolver
from dns import reversename
from threading import Thread
from threading import Lock
import sys

startip = "137.73.130.0"[:-1]
# name , alias, addresslist =socket.gethostbyaddr('ip')
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
list = ["2.2.2.2","3.3.3.3","4.4.4.4","5.5.5.5","8.8.8.8","114.114.114.114"]
dnslist = ["ns1.borwood.net","ns4.vispa.net.uk","ns1.swisp.co.uk","ns1.bt.es","ns3.brookcom.net"].append(list)

def GetDnsPtrRecord(ip_list=[],outfile = sys.stdout, result=None, lock=None,dnslist=None):
    ret_data = []
    for i in ip_list:
        #print(i,end=':',file = outfile)
        try:
    #        name , alias, addresslist = socket.gethostbyaddr(i)
            addr = reversename.from_address(i)
            resolver.timeout = 1
            resolver.nameservers = dnslist
            out = resolver.query(addr,"PTR")
        except Exception as e :
            #print('',file=outfile)
            tmp = i+": Unable to get"
            ret_data.append(tmp)
            continue #print(name,file=outfile)
        tmp = i+': '
        for record in range(len(out)):
            tmp= tmp+str(out[record])+':'
            if dnslist is not None:
                dnslist.append(str(out[record])[:-1])

        ret_data.append(tmp)

# determine output format
    if result is not None:
        if lock is not None:
            lock.acquire()
        for i in ret_data:
            result.append(i)
        if lock is not None:
            lock.release()
        
    else :
        for i in ret_data:
            print(i,file=outfile)


def PtrRecord(ip_list=[], outfile =sys.stdout, multiThread=256):
    global dnslist
    data = []
    threads = []
    results = []
    length = len(iplist)//multiThread
    for i in range(multiThread-1):
        data.append(iplist[i*length:(i+1)*length])
    data.append(iplist[(multiThread-1) *length:])
    
    lck = Lock()
#Defining threads
    for i in range(multiThread):
        threads.append(Thread( target=GetDnsPtrRecord, kwargs=dict(ip_list=data[i],outfile=None,result=results,lock= lck,dnslist= dnslist)) )
#Start threads
    for t in threads:
        t.start()
#Wait for threads
    for j in threads:
        j.join()
    return results,dnslist
    



f = open(sys.argv[1],'r')
iplist = []
#103.235.46.39
for i in f:
    iplist.append(i[:-1])


for i in PtrRecord()[0]:
    if(i.find('Unable')==-1):
        print(i[:-2])

#flck = Lock()
#def _thread_get_robot(domains=[],file=None):
#    for i in domains:
#        try:
#            ret  = requests.get('http://'+i+'/', verify=False, timeout=8)
#            if ret.status_code == 200:
#                print('[*] get '+i)
#                print('yes')
#                txt = ret.text
#                if file is not None:
#                    flck.acquire()
#                    file.write(i+' \'s title: '+txt[txt.find('<title>')+7, txt.find('</title')])
#                    file.flush()
#                    flck.release()
#                #f = open(i+'.robot','w+')
#                #f.write(ret.text)
#                #f.close()
#            else:
#                print('[*] get '+i)
#                print(ret.status_code)
#        except Exception as e:
#            print('[*] get '+i)
#            print("time out")
#            continue
#t_cnt = 8
#t_domains =[]
#d_cnt=len(domains)//t_cnt 
##print(len(domains))
#threads = []
#for i in range( t_cnt-1):
#    t_domains.append( domains[i*d_cnt: (i+1)*d_cnt])
#
#t_domains.append(domains[ (t_cnt-1)*d_cnt:])
#
##print(t_domains)
#
#outfile = open('./data.txt','a+')
#for i  in range(t_cnt):
#    threads.append(Thread( target=_thread_get_robot, kwargs=dict(domains=t_domains[i],file =outfile )))
#    threads[i].start()
#for i in threads:
#    i.join()
#outfile.close()
#
#
#
