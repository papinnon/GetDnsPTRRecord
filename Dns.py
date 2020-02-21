import requests
import socket
import urllib3
from dns import resolver
from dns import reversename
import threading 
import sys
import queue

list = ["114.114.114.114"]
dnslist=["151.250.94.140"].append(list)
debug=0
def miniGetDnsPtrRecord(ip, timeout=5.0):
    global dnslist
    try:
        addr = reversename.from_address(ip)
        resolver.timeout=timeout
        out=        resolver.query(addr, "PTR")
    except Exception as e :
        #print(e)
        out = ip+": Failed."
        return out
    #print(out[len(out)-1])
    #print(ip)
    tmp= "{:15}: {}".format(ip,out[len(out)-1]) 
    return tmp

def thread_cb(timeout ):
    global q 
    global res
    while(True):
        try:
            target = q.get_nowait()
            result = miniGetDnsPtrRecord(target,timeout=timeout)
            res.append(result)
        except queue.Empty:
            if (debug ==1):
                print("Queue Empty Exiting...");
            break
    return   


def tp_GetDnsPtrRecord(ips=[], n_threads=256,  timeout=5.0):
    for i in ips:
        q.put(i)
    threads=[]
    for i in range(n_threads):
        threads.append( threading.Thread(target=thread_cb, kwargs={'timeout':timeout}))
        threads[i].start()  

    for i in range(n_threads):
        threads[i].join()


q = queue.Queue()
res=[]

f = open(sys.argv[1],'r')
ips=[]
for i in f:
    ips.append(i[:-1])

tp_GetDnsPtrRecord(ips)
for i in res:
    print(i)
