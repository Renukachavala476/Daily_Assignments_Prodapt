import threading,time
def primenumber():
    for i in range(2,500):
       if i>1:
           for a in range(2,i):
               if(i%a)==0:
                   break
           else:
                print(i,end=' ')
def palindromenum():
    rev=0
    temp=num
    while temp>0:
        rev=(rev*10)+(temp%10)
        temp=temp//10
    return rev==num
for num in range(2,500):
    if palindromenum():
        print(num,end=' ')
t1=threading.Thread(target=primenumber)#creating a thread
t2=threading.Thread(target=palindromenum)
t1.start()
t2.start()
t1.join()
t2.join()



    