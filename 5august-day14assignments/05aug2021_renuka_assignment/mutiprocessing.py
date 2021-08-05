import time,multiprocessing
def findsquare(getlist):
    for i in getlist:
        time.sleep(1)
        print(i*i)
def findcube(getlist):
    for i in getlist:
        time.sleep(1)
        print(i*i*i)
if(__name__=='__main__'):

    mylist=[32,23,79,46,]
    p1=multiprocessing.Process(target=findsquare,args=(mylist,))
    p2=multiprocessing.Process(target=findcube,args=(mylist,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()