l=[]
while True :
 c=int(input('''
1  Push Element
2  Pop Element
3  Front Element
4  Last Element
5  Display Queue
6  Exit
'''))

 if c==1 :
    a=input("enter element to be Pushed :")
    l.append(a)
    print(l)
 elif c==2 :
    if len(l)==0 :
        print("Queue empty...")
    else :
        b=l.pop(0)
        print("your pop element is",b)
        print("Modify queue after Pop is ",l)
 elif c==3 :
    if len(l)==0 :
        print("Queue empty...")
    else :
        print("Front element is ",l[0])
 elif c==4 :
    if len(l)==0 :
        print("Queue empty...")
    else :
      print("Last element is",l[-1])
 elif c==5 :
    if len(l)==0 :
        print("Queue empty...")
    else :
        print("Your Present Queue is ",l)
 elif c==6 :
    break ;
 else :
    print("Invaild Operation....")


