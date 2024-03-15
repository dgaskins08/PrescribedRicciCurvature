from sympy import *
from sympy import Matrix
from sympy.abc import a, b,c,d
from so17orthonormalbasis import *

#This file checks that I have a decomposition for so(1,7) = g2 + p_1 + p_2
#The one thing that is not checked is that when I take the g2 I get from Maple and place it in so(1,7) that it is still g2.
#One can eye-ball it if needed, but all I am doing is placing a row of 0's and a column of 0's above and to the left of the matrices in g2
#This does not change bracket relations or dimension, so I am still in g2.


#The ordering of the checks:
#First, we check that g2 + p_1 is in so(7) and an orthogonal decomposition
#Second, we check that so(7) + p_2 is an orthogonal decomposition and that p_2 matches Helgason's definition in Ch. X
#Third, we check that p_1 has an orthonormal decomposition
#Fourth, we check that p_2 has an orthonormal decomposition
#Last, we check that so(1,7) has the right dimension of 28
#The only other thing one might want to check is that the so(7) is in the bottom right block and the p_2 consists of E_1i + E_i1, this is an easy check by the eye or you can look at the source code


#This is the so(1,7) basis whose first 14 entries are the G2 above but placed in so(1,7) instead of just so(7)
#The next 14 entries make up p_1 and p_2 (7 dim each)
so17Basis

#G2 in so(1,7)
G28

#p_1
P1

#p_2
P2





print("Check 1: G28 + P1, are they orthogonal commplements in so(7) and are there enough elements to span?")
#Check that G28 and p_1 are orthogonal under trace(uv) and are in so(7) inside so(1,7)
#If you get an "uh oh for G28 and p1" then you are not in so(7)
#If you get something besides [0,21], you don't have orthogonality (the 0) or enough to span (the 21)
sum = 0
for x in G28:
    for y in P1:
        if transpose(x) == -x and transpose(y) == -y:
            sum = sum + trace(x*y)
        else:
            print("uh oh for G28 and p1")
            print([x,y])
print("no uh oh message? Success, your elements are skew symmetric!")
print("If there is an uh oh message, then the pair [x,y] that comes with it are the elements in G28 and P1 respectively that are not in so(7)")
print([sum, len(G28 + P1)])
print("If the pair above is [0, 21] then you have orthogonality between elements in G28 and P1 and there are 21 elements in G28 + P1")
print("If the first number is not 0, you don't have an orthogonal complement")
print("If the second number is not 21 then you don't have enough elements to span so(7)")



K = G28 + P1


print("Check 2: Is P2 orthogonal to the maximal compact so(7) = K and are there enough elements to span so(1,7)?")
#Checking that P2 is orthogonal to the maximal compact so(7) = K
#Also checking that P2 is as defined in Helgason
#If you get an "uh oh for p2" then it is not defined as in Helgason
#If you get a number other than [0, 7] then you don't have orthogonality (the 0) or enough to span (the 7)
sum = 0
for x in K:
    for y in P2:
        if transpose(y) == y:
            sum = sum + trace(x*y)
        else:
            print("uh oh for P2")
            print(y)
print("no uh oh message? Success! Your elements are symmetric!")
print("If there is an uh oh message then the element that comes with it is not in p_2")
print([sum, len(P1)])
print("If the above [x,y] is [0,7] then you have P2 as an orthogonal complement to K and K + P2 has enough elements to span so(1,7)")
print("If not x in [x,y] is not 0 then you don't have an orthogonal complement and if y is not 28 then you don't have enough elements to span so(1,7)")


print("Check 3: Are P1 and P2 elements orthonormal for their respective metrics?")
#Checking orthonormality of P1 using the metric defined in called file
#If the sum is anything other than 0 orthogonality is a problem
#If "uh oh P1 not orthonormal" appears then the element is not norm 1
sum = 0
for x in P1:
    for y in P1:
        if x == y:
            if metric(x,y) == 1:
                pass
            else:
                print("uh oh P1 not orthonormal")
                print(x)
        else:
            sum = sum + metric(x,y)
print("If no uh oh message for P1 then your norms are 1! Otherwise, the element given is not normalized for the metric")
print(sum)
print("If the number above is not 0 then you don't have orthogonality in P1!")



#Checking orthonormality of P2 using the metric defined in called file
#If the sum is anything other than 0 orthogonality is a problem
#If "uh oh P2 not orthonormal" appears then the element is not norm 1
sum = 0
for x in P2:
    for y in P2:
        if x == y:
            if metric1(x,y) == 1:
                pass
            else:
                print("uh oh P2 not orthonormal")
                print(x)
        else:
            sum = sum + metric(x,y)
print("If no uh oh message for P2 then your norms are 1! Otherwise, the element given is not normalized for the metric")
print(sum)
print("If the number above is not 0 then you don't have orthogonality in P2!")

#This checks how many elements are in so17, I expect 28
print(len(so17Basis))


