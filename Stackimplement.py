l=[]
while True :
    c=int(input('''
    1 Push_elements
    2 pop_elements
    3 peek_element
    4 Diaplay_stack
    5 Exit 
    '''))
    if c==1 :
        a=input("enter element to be pushed :")
        l.append(a)
        print(l)
    elif c==2 :
        if len(l)==0 :
            print('Empty Stack')
        else :
           p=l.pop()
           print("pop element is : " ,p)
           print(l)
    elif c==3 :
        if len(l)==0 :
            print('Empty Stack')
        else :
            print("The peek element is :",l[-1])
    elif c==4 :
        if len(l)==0 :
            print('Empty Stack')
        else :
            print("The stack is ",l)
    elif c==5 :
        break ;
    else :
        print("invalid opration...")