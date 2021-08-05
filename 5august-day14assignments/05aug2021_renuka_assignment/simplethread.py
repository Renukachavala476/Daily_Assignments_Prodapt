import threading,time
def printnumbers():
    for i in range(1,10):
        time.sleep(1)
        print(i)
def printhello():
    for i in range(1,4):
        time.sleep(1)
        print("hello")
t1=threading.Thread(target=printnumbers)#creating a thread
t2=threading.Thread(target=printhello)
t1.start()
t2.start()
t1.join()
t2.join()
print("............")

