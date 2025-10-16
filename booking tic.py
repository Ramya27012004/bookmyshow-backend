def singleton(arg):
    L=[]
    def inner():
        if len(L)==0:
            ob=arg()
            L.append(ob)
        return L[0]
    return inner
@singleton
class Movie1():
    def __init__(self):
        self.maxtic=150
    def Booking(self):
        print(f'avuaiable tickets are:{self.maxtic}')
        count=int(input("enter the number of tic:"))
        if 0<count<=self.maxtic:
            self.maxtic-=count
            print("booking successful...")
        else:
            print("invalid input")
@singleton
class Movie2():
    def __init__(self):
        self.maxtic=250
    def Booking(self):
        print(f'avuaiable tickets are:{self.maxtic}')
        count=int(input("enter the number of tic:"))
        if 0<count<=self.maxtic:
            self.maxtic-=count
            print("booking successful...")
        else:
            print("invalid input")
@singleton
class Movie3():
    def __init__(self):
        self.maxtic=200
    def Booking(self):
        print(f'avuaiable tickets are:{self.maxtic}')
        count=int(input("enter the number of tic:"))
        if 0<count<=self.maxtic:
            self.maxtic-=count
            print("booking successful...")
        else:
            print("invalid input")
def Bmys():
   print('1.Movie1\n2.Movie2\n3.Movie3')
   choice=int(input("enter the Movie:"))
   if choice==1:
       obj1=Movie1()
       obj1.Booking()
   elif choice==2:
       obj2=Movie2()
       obj2.Booking()
   elif choice==3:
         obj3=Movie3()
         obj3.Booking()
   else:
        print("invalid input")
def payTM():
    print('1.Movie1\n2.Movie2\n3.Movie3')
    choice=int(input("enter the Movie:"))
    if choice==1:
        obj1=Movie1()
        obj1.Booking()
    elif choice==2:
        obj2=Movie2()
        obj2.Booking()
    elif choice==3:
            obj3=Movie3()
            obj3.Booking()
    else:
            print("invalid input")
user1=Bmys()
user2=payTM()
user3=Bmys()
user4=payTM()