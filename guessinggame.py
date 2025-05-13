import random
while True :
 print('''
 1 - 100 : Choose number to play game
  101    : End game  
 ''')
 c=random.randint(1,100)
 i=int(input("enter your number:"))
 if i<=100 :
   if i<c :
    if c-i<10 :
        print("your number is low")
        print("computer number is",c)
    else:
        print("your number is too low")
        print("computer number is", c)
   elif i>c  :
    if i-c<10 :
        print("your number is high")
        print("computer number is", c)
    else :
        print("your number is too high")
        print("computer number is", c)
   elif i==c :
    print("Both number match")
    print("congrats you won !!")


 if i==101 :
     print("game end...")
     break;
 elif i>101 :
     print("invalid operation...")