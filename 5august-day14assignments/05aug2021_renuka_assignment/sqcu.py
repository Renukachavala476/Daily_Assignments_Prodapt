import threading,time
def findsquare(getlist):
    for i in getlist:
        time.sleep(1)
        print(i*i)
def findcube(getlist):
    for i in getlist:
        time.sleep(1)
        print(i*i*i)
mylist=[2,3,4,5]
t1=threading.Thread(target=findsquare,args=(mylist,))#creating a thread
t2=threading.Thread(target=findcube,args=(mylist,))
t1.start()
t2.start()
t1.join()
t2.join()
print("............")
