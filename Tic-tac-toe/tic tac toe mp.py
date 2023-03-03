import mysql.connector as mc

mydb=mc.connect(host="localhost",user="adharsh",passwd="1234")
cursor=mydb.cursor()

while(True):
    n1=input("Enter username 1:")
    p1=int(input("Enter the password:"))


    cursor.execute("""use csa""")
    cursor.execute("""select pwd from clasSic where rollno=%s""",(n1,))

    res=cursor.fetchone()
    q=res[0]

    if q==p1:
        print("Player 1 granted")
        print()
        print()
        d=0
        break
    else:
        print("Invalid password or username")
        print()
        print()
        continue
while(True):
    n2=input("Enter username 2:")
    p2=int(input("Enter the password:"))

    
    cursor.execute("""use csa""")
    cursor.execute("""select pwd from clasSic where rollno=%s""",(n2,))

    res=cursor.fetchone()
    q=res[0]

    if q==p2:
        print("Player 2 granted")
        print()
        print()
        break
    else:
        print("Invalid password or username")
        print()
        print()
        continue

cursor.execute("""select namess from classic where pwd=%s""",(p1,))
d1=cursor.fetchone()
d1=d1[0]

cursor.execute("""select namess from classic where rollno=%s""",(n2,))
d2=cursor.fetchone()
d2=d2[0]

cursor.execute("""select games from classic where rollno=%s""",(n1,))
g1=cursor.fetchone()
g1=g1[0]

cursor.execute("""select games from classic where rollno=%s""",(n2,))
g2=cursor.fetchone()
g2=g2[0]

cursor.execute("""select highscore from classic where rollno=%s""",(n1,))
hs1=cursor.fetchone()
hs1=hs1[0]

cursor.execute("""select highscore from classic where rollno=%s""",(n2,))
hs2=cursor.fetchone()
hs2=hs2[0]

print("Hi ! Welcome to TIC TAC TOE")

k='''
-------------
| 1 | 2 | 3 |
-------------
| 4 | 5 | 6 |
-------------
| 7 | 8 | 9 |
------------- '''



print()
print()
print("                              {}  VS  {}".format(d1,d2))
print()
print("Games played:                 {}  --  {}".format(g1,g2))
print()
print("Battles won:                  {}  --  {}".format(hs1,hs2))


kk=k


score=0
cscore=0

#winning combinations
set1={'1','2','3'}
set2={'4','5','6'}
set3={'7','8','9'}
set4={'1','5','9'}
set5={'1','4','7'}
set6={'2','5','8'}
set7={'3','6','9'}
set8={'3','5','7'}



def s1(s):
    s=s.intersection(set1)
    s=sorted(s)
    s=set(s)
    return s

def s2(s):
    s=s.intersection(set2)
    s=sorted(s)
    s=set(s)
    return s

def s3(s):
    s=s.intersection(set3)
    s=sorted(s)
    s=set(s)
    return s
def s4(s):
    s=s.intersection(set4)
    s=sorted(s)
    s=set(s)
    return s
def s5(s):
    s=s.intersection(set5)
    s=sorted(s)
    s=set(s)
    return s
def s6(s):
    s=s.intersection(set6)
    s=sorted(s)
    s=set(s)
    return s
def s7(s):
    s=s.intersection(set7)
    s=sorted(s)
    s=set(s)
    return s
def s8(s):
    s=s.intersection(set8)
    s=sorted(s)
    s=set(s)
    return s


while(True):
    print(kk)
    print()
    choice=input("Please enter the choice of player 1 as X/O:")
    d=choice.capitalize()
    print("{} going to play as:".format(d1),d)
    print()
    print()
    if(d=="X"):
        print("{} going to play as: O".format(d2))
        u=set()
        v=set()
        for i in range(1,6,1):
            print()
            n=input("Enter a number from 1 to 9:")
            if n not in u and n not in v:
                u.add(n)
                u=sorted(u)
                u=set(u)
                k=k.replace(n,"X")
                print(k)
            elif n in u or n in v:
                print("This number as already entered")
                continue

            chckset1=s1(u)
            chckset2=s2(u)
            chckset3=s3(u)
            chckset4=s4(u)
            chckset5=s5(u)
            chckset6=s6(u)
            chckset7=s7(u)
            chckset8=s8(u)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Player 1 wins the game")
                score+=1
                k=kk
                break
            

            if i==5:
                print()
                print("The Game ends in a draw")
                k=kk
                break
        
            print()
            n=input("Enter a number from 1 to 9:")
            if n not in u and n not in v:
                     v.add(n)
                     v=sorted(v)
                     v=set(v)
                     k=k.replace(n,"O")
                     print(k)
            elif n in u or n in v:
                print("This number as already entered")
                continue
         
            chckset1=s1(v)
            chckset2=s2(v)
            chckset3=s3(v)
            chckset4=s4(v)
            chckset5=s5(v)
            chckset6=s6(v)
            chckset7=s7(v)
            chckset8=s8(v)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Player 2 wins the game")
                cscore+=1
                k=kk
                break
            
    elif d=="O":
        u=set()
        v=set()
        for i in range(1,6,1):            
            print()
            print("{} going to play as: X".format(d2))
            n=input("Enter a number from 1 to 9:")
            if n not in u and n not in v:
                u.add(n)
                u=sorted(u)
                u=set(u)
                k=k.replace(n,"X")
                print(k)
            elif n in u or n in v:
                print("This number as already entered")
                continue
         
            chckset1=s1(u)
            chckset2=s2(u)
            chckset3=s3(u)
            chckset4=s4(u)
            chckset5=s5(u)
            chckset6=s6(u)
            chckset7=s7(u)
            chckset8=s8(u)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                k=kk
                print("Player 2 wins the game")
                cscore+=1
                break
            if i==5:
                print()
                print("The Game ends in a draw")
                k=kk
                break
            while(True):
               print()
               n=input("Enter a number from 1 to 9:")
               if n not in u and n not in v:
                    v.add(n)
                    v=sorted(v)
                    v=set(v)
                    k=k.replace(n,"O")
                    print(k)
                    break
               elif n in u or n in v:
                    print()
                    print("This number as already entered")
                    continue

            chckset1=s1(v)
            chckset2=s2(v)
            chckset3=s3(v)
            chckset4=s4(v)
            chckset5=s5(v)
            chckset6=s6(v)
            chckset7=s7(v)
            chckset8=s8(v)
            if chckset1==set1 or chckset2==set2 or chckset3==set3 or chckset4==set4 or chckset5==set5 or chckset6==set6 or chckset7==set7 or chckset8==set8:
                print()
                print("Player wins the game")
                k=kk
                score+=1
                break
    else:
        print()
        print("Please enter a valid choice")
        continue

    x=input("Do you wish to continue  yes/no:")
    x=x.capitalize()
   
    if x=="Yes" or x=="Y":
        continue
    elif x=="No" or x=="N": 
        if score==cscore:
            print()
            print("Player 1 score =",score)
            print()
            print("Player 2 score =",cscore)
            print()
            g1+=1
            cursor.execute("""UPDATE classic SET games=%s WHERE rollno=%s""",(g1,n1))
            g2+=1
            cursor.execute("""UPDATE classic SET games=%s WHERE rollno=%s""",(g2,n2))
            mydb.commit()

            print("The battle is tied")
        elif score>cscore:
            print()
            print("Player 1 score = ",score)
            print()
            print("Player 2 score = ",cscore)
            print()
            print("Player wins the battle")
            hs1+=1
            cursor.execute("""UPDATE classic SET highscore=%s WHERE rollno=%s""",(hs1,n1))
            g1+=1
            cursor.execute("""UPDATE classic SET games=%s WHERE rollno=%s""",(g1,n1))
            g2+=1
            cursor.execute("""UPDATE classic SET games=%s WHERE rollno=%s""",(g2,n2))
            mydb.commit()
            
        else:
            print()
            print("Player 1 score = ",score)
            print()
            print("Player 2 score = ",cscore)
            print()
            print("Player 2 wins the battle")
            hs2+=1
            cursor.execute("""UPDATE classic SET highscore=%s WHERE rollno=%s""",(hs2,n2))
            g1+=1
            cursor.execute("""UPDATE classic SET games=%s WHERE rollno=%s""",(g1,n1))
            g2+=1
            cursor.execute("""UPDATE classic SET games=%s WHERE rollno=%s""",(g2,n2))
            mydb.commit()
        print()
        print("Thank you for playing this game")
        break
