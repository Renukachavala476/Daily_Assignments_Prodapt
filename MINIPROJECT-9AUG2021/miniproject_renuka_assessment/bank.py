import re,csv,logging,json
try:
    header =['customerid','customername','amount']
    banklist=[]
    def validate(customername):
    
        cname=re.search("^[A-Za-z]{2,25}$",customername)
    
        if cname:
            return True
        else:
            return False

    class BankCustomer:
     
        def addCustomer(self,customername,customerid,amount):
            cusdict={"customerid":customerid,"customername":customername,"amount":amount}
            banklist.append(cusdict)
    obj1=BankCustomer() 
    while(True):
        print("1.add customer details")      
        print("2.view customers")
        print("3.search customer by customerid")
        print("4.display amount")
        print("5.generate csv file")
        print("6.generate json file")
        print("7.exit")
        choice=int(input("Enter your choice:"))
        if choice==1:
            customerid=int(input("enter customer id"))
            customername=input("enter customer name")
            amount=int(input("enter deposit amount"))
            x=validate(customername)
            if x:
                obj1.addCustomer(customername,customerid,amount)
            else:
                logging.error("please enter valid details")
        if choice==2:
            print(banklist)
        if choice==3:
            cusid=int(input("enter required customer id"))
            print(list(filter(lambda i:i["customerid"]==cusid,banklist)))
        if choice==4:
            wamt=int(input("enter withdraw amount"))
            tamnt=amount-wamt
            print(tamnt)      
        if choice==5:
            with open('banklist.csv','w+',encoding='UTF8',newline='') as s:
                writer = csv.DictWriter(s,fieldnames=header)
                writer.writeheader()
                writer.writerows(banklist)
        if choice==6:
            data=(sorted(banklist,key=lambda i:i["amount"],reverse=True))
            print(data)
            myjson=json.dumps(banklist) 
            with open('bank.json','w',encoding="utf-8") as b:
                b.write(myjson)
        if choice==7:
            break
except:
    logging.error("enter valid credentials")