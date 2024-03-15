from so17orthonormalbasis import *
from IntertwiningMap import *

#Now to create the ad maps for the p_1 and p_2 parts
#Since ad will now have some g_2 in it, we will need to just take the inner product value for the matrix values
#Other than that, it is the same process for the adp_1 as it was for the adg2
#For adp_2, by Cartan decomposition properties, it will be top right and bottom left blocks with values, so the metric usages must change
adpmat = []
k = 14
while 13 < k < 21: #Selecting an element from p_1 to calculate ad for that element
    adp = zeros(14, 14)
    i = 14
    while 13 < i < 21:
        BR = bracket(so17Basis[k], so17Basis[i]) #if x in p_1 then [x,y] has a component in p_1 for y in p_1 so we use the metric on p_1 here
        j = 14
        while 13 < j < 21:
            if trace(BR*so17Basis[j]) == 0:
                pass
            else:
                adp[j-14, i-14] = metric(BR, so17Basis[j])
            j = j+1
        i = i + 1


    i = 21
    while 20 < i < 28:
        BR = bracket(so17Basis[k], so17Basis[i]) #if x in p_1 then [x,y] is in p_2 for y in p_2 so we use the metric on p_2 here
        j = 21
        while 20 < j < 28:
            if trace(BR*so17Basis[j]) == 0:
                pass
            else:
                adp[j - 14, i - 14] = S(6)*trace(BR*so17Basis[j])
            j = j +1
        i = i +1
    adpmat = adpmat + [adp]
    k = k +1

#For the second 7, by the Cartan properties, the ad maps will send p_1 to p_2 and p_2 to p_1.
k = 21
while 20 < k < 28:
    adp = zeros(14, 14)
    i = 14
    while 13 < i < 21:
        BR = bracket(so17Basis[k], so17Basis[i])
        j = 21
        while 20 < j < 28:
            if trace(BR*so17Basis[j]) == 0:
                pass
            else:
                adp[j - 14, i - 14] = S(6)*trace(BR*so17Basis[j])
            j = j + 1
        i = i +1

    i = 21
    while 20 < i < 28:
        BR = bracket(so17Basis[k], so17Basis[i])
        j = 14
        while 13 < j < 21:
            if trace(BR*so17Basis[j]) == 0:
                pass
            else:
                adp[j-14, i-14] = metric(BR, so17Basis[j])
            j = j+1
        i = i + 1
    adpmat = adpmat + [adp]
    k = k + 1


Phi_inv = Phi.inv()






#x and y are vectors of length 14
#phi is any 14 by 14 matrix but we want it to be an intertwining map
#admaps is all the ad_p maps
def Term1(x,y, phi, admaps):
    sum = 0
    i = 0
    phi_inv = phi.inv()
    while i < 14:
        ad = zeros(14,14)
        k = 0
        while k < 14:
            ad = ad + phi_inv[k,i]*admaps[k]
            k = k +1
        first = phi*ad*x
        second = phi*ad*y
        sum = sum + first.dot(second)
        i = i + 1
    return(sum)

#x and y are vectors of lenght 14
#phi is any 14 by 14 matrix but we want it to be an intertwining map
#admaps is all the ad_p maps
#PBasis1 is the standard orthonormal basis in R^14

def Term3(x, y, phi, admaps, PBasis1):
    sum = 0
    j = 0
    phi_inv = phi.inv()
    while j < 14:
        i = 0
        while i < 14:
            ad = zeros(14,14)
            k = 0
            while k < 14:
                ad = ad + phi_inv[k, i]*admaps[k]
                k = k +1
            first = phi*ad*phi_inv*PBasis1[j] #The left part of the inner product in both pieces
            second = phi*x #The right part of the inner product in the first inner product
            third = phi*y #The right part of the inner product in the second inner product
            sum = sum + (first.dot(second))*(first.dot(third))
            i = i +1
        j = j +1
    return(sum)

#Killing here will take x and y the same as the other terms, but will first produce the matrices in so(1,7) corresponding to x and y
#Using the matrices, we utilize that B(.,.) = 6tr(..)
def Killing(x,y, PBasis2):
    i = 0
    mx = zeros(8,8)
    my = zeros(8,8)
    while i < 14:
        mx = mx + x[i]*PBasis2[i]
        my = my + y[i]*PBasis2[i]
        i = i + 1
    tr = trace(mx*my)
    return(6*tr)

def ric(x,y, phi, admaps, PBasis1, PBasis2):
    rxy = S(-1)/2*Term1(x,y, phi, admaps) + S(1)/4*Term3(x, y, phi, admaps, PBasis1) - S(1)/2*Killing(x,y, PBasis2)
    return(rxy)

M = eye(14,14)
E_1 = M.col(0)
E_2 = M.col(1)
E_3 = M.col(2)
E_4 = M.col(3)
E_5 = M.col(4)
E_6 = M.col(5)
E_7 = M.col(6)
E_8 = M.col(7)
E_9 = M.col(8)
E_10 = M.col(9)
E_11 = M.col(10)
E_12 = M.col(11)
E_13 = M.col(12)
E_14 = M.col(13)

#This creates our standard basis with a 1 in the ith spot
PBasis1 = [E_1, E_2, E_3, E_4, E_5, E_6, E_7, E_8, E_9, E_10, E_11, E_12, E_13, E_14]

#This selects our orthonormal basis for p = p_1 + p_2
PBasis2 = so17Basis[14:28]


#r1 = ric(PBasis1[0],PBasis1[0], Phi_inv, adpmat, PBasis1, PBasis2)
#r2 = ric(PBasis1[8],PBasis1[8], Phi_inv, adpmat, PBasis1, PBasis2)
#r3 = ric(PBasis1[0],PBasis1[7], Phi_inv, adpmat, PBasis1, PBasis2)

#r1 = simplify(r1)
#r1 = simplify(r1)
#print(mathematica_code(r1))
#r2 = simplify(r2)
#r2 = simplify(r2)
#print(mathematica_code(r2))
#r3 = simplify(r3)
#r3 = simplify(r3)
#print(mathematica_code(r3))


T1 = Term3(PBasis1[0],PBasis1[0], Phi_inv, adpmat,PBasis1)
T2 = Term3(PBasis1[8],PBasis1[8], Phi_inv, adpmat, PBasis1)
T3 = Term3(PBasis1[0],PBasis1[7], Phi_inv, adpmat, PBasis1)

T1 = simplify(T1)
T1 = simplify(T1)
print(mathematica_code((T1)))

T1 = simplify(T2)
T1 = simplify(T2)
print(mathematica_code((T2)))


T1 = simplify(T2)
T1 = simplify(T2)
print(mathematica_code((T2)))


#It is Term3 has degree 8 but Term1 has degree 4 that is giving the extra powers, so it is Term 3 that needs to be simplified.
