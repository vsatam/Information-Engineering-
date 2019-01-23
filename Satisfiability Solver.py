#SAT. THE SAME PROBLEM CAN BE CONVERTED TO 3 SAT BY JUST CHANGING MATRIX DIMENSIONS OF 'a'.


def TF(A):                      #Function to convert 1 to True and -1 to False acc to given condition.
    for i in range(0, len(A)):
        if A[i] == 1:
            A[i] = True
        elif A[i] == -1:
            A[i] = False
        elif A[i]==0:           # 0 are replaced by 2 as 0 themselves represent False on python.
            A[i]=2
    return A

import numpy as np
a = np.random.randint(-1, 2, size=(5, 5));      #Creating random 5*5 Matrix.

print(a)

C1=TF(list(a[0]))                               #Obtaining Clauses
C2=TF(list(a[1]))
C3=TF(list(a[2]))
C4=TF(list(a[3]))
C5=TF(list(a[4]))
print(C1)
print(C2)
print(C3)
print(C4)
print(C5)
for j in range(0, 32):                  #Obtaining Bit values from dec
    d = bin(j)[2:].zfill(5)
    c = list(d)
    D = []
    for i in range(0, 5):
        if c[i] == '0':
            D.append(False)
        elif c[i] == '1':
            D.append(True)
    Z1 = False
    Z2 = False
    Z3 = False
    Z4 = False
    Z5 = False
    for i in range(0, 5):
        if (C1[i] == True and D[i] == True) or (C1[i] == False and D[i] == True):   #Next statements explain logic of clauses
            Z1 = True
        elif C1[i] == 2:
            continue
        elif Z1 == True:
            break
    for i in range(0, 5):
        if (C2[i] == True and D[i] == True) or (C2[i] == False and D[i] == True):
            Z2 = True
        elif C2[i] == 2:
            continue
        elif Z2 == True:
            break
    for i in range(0, 5):
        if (C3[i] == True and D[i] == True) or (C3[i] == False and D[i] == True):
            Z3 = True
        elif C3[i] == 2:
            continue
        elif Z3 == True:
            break
    for i in range(0, 5):
        if (C4[i] == True and D[i] == True) or (C4[i] == False and D[i] == True):
            Z4 = True
        elif C4[i] == 2:
            continue
        elif Z4 == True:
            break
    for i in range(0, 5):
        if (C5[i] == True and D[i] == True) or (C5[i] == False and D[i] == True):
            Z5 = True
        elif C5[i] == 2:
            continue
        elif Z5 == True:
            break
    Z = Z1 and Z2 and Z3 and Z4 and Z5;         #Condition to check if D is a solution.
    if Z == False:
        print( d, 'is not a solution')
    else:
        pass
