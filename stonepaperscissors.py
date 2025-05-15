import random
l=['Stone','Paper','Scissor']
a=b=d =0
e=1
while True :
    print("ROUND",e,"/5")
    print("select your pref...:")
    i=int(input('''
    1  Stone
    2  Paper
    3  Scissor
    '''))
    c=random.choice(l)
    a=a+1
    e=e+1
    if c=='Stone' :
        if i==1 :
            print("Draw...")
            print("Both you and computer have Selected Stone..")
            b= b + 1
            d= d + 1
        if i==2  :
            print("Computer won")
            print("Computer has selected Stone & You have selected Scissor..")
            b = b + 1
            d = d + 0
        if i==3  :
            print("You won")
            print("Computer has selected Stone & You have selected Paper..")
            b = b + 0
            d = d + 1
    if c == 'Paper':
        if i == 2:
            print("Draw...")
            print("Both you and computer have Selected Paper..")
            b = b + 1
            d = d + 1
        if i == 1:
            print("Computer won")
            print("Computer has selected Paper & You have selected Stone..")
            b = b + 1
            d = d + 0
        if i == 3:
            print("You won")
            print("Computer has selected Paper & You have selected Scissor..")
            b = b + 0
            d = d + 1
    if c == 'Scissor':
        if i == 3:
            print("Draw...")
            print("Both you and computer have Selected Scissor..")
            b = b + 1
            d = d + 1
        if i == 2:
            print("Computer won")
            print("Computer has selected Scissor & You have selected Paper..")
            b = b + 1
            d = d + 0
        if i == 1:
            print("You won")
            print("Computer has selected Scissor & You have selected Stone..")
            b = b + 0
            d = d + 1
    if a==5 :
        print("THE FINAL RESULT AFTER 5 ROUND:")
        if b==d :
            print("Game Draw....")
            print("your score is ",d)
            print("Computer score is ",b)
            break
        if b>d :
            print("Computer Won....")
            print("your score is ", d)
            print("Computer score is ", b)
            break
        if b<d :
            print("You Won....")
            print("your score is ", d)
            print("Computer score is ", b)
            break

