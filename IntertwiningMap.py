from so17orthonormalbasis import *

#This is the so(1,7) basis whose first 14 entries are the G2 above but placed in so(1,7) instead of just so(7)
#The next 14 entries make up p_1 and p_2 (7 dim each)
so17Basis

#G2 in so(1,7)
G28

#p_1
P1

#p_2
P2



#First we build our adg2 matrices and we do so in one big loop
#We build our matrix by using the inner product. That is M_ij = <Mej, e_i> for a matrix M and an orthonormal basis with respect to <.,.>
#The result of this process is a list of matrices that are 14x14 with the top left 7x7 going to p_1 and the bottom right going to p_2
admat = []
k = 0
while k < 14: #This loop is selecting basis elements from G28 to enter ino the bracket
    adg = zeros(14,14)
    i = 14
    while 13 < i < 21: #This loop is selecting basis elements from p_1 for the bracket
        BR = bracket(so17Basis[k], so17Basis[i]) #bracket is called from so17orthonormalbasis.py
        j = 14
        while 13 < j < 21:
            if metric(BR, so17Basis[j]) == 0: #metric(.,.) is called from so17orthonormalbasis.py
                pass
            else:
                adg[j-14, i-14] = metric(BR, so17Basis[j])
            j = j+1
        i = i + 1

    i = 21 #This loop is selecting basis elements from p_2 for the bracket
    while 20 < i < 28:
        BR = bracket(so17Basis[k], so17Basis[i])
        j = 21
        while 20 < j < 28:
            if S(6) * trace(BR * so17Basis[j]) == 0: # Here we can't call metric1 because BR will be a scalar multiple of a basis element.
                pass
            else:
                adg[j - 14, i - 14] = S(6) * trace(BR * so17Basis[j])
            j = j +1
        i = i +1
    admat = admat + [adg]
    k = k +1





Psi = zeros(14, 14)
Psi[7,0] = c
Psi[8, 1] = c
Psi[9, 2] = c
Psi[10, 3] = c
Psi[11, 4] = c
Psi[12, 5] = c
Psi[13, 6] = c


#We make it symmetric since we ultimately want that
Psi = Psi + transpose(Psi)

#Here we get our multiple of the identity for the top left and top right
#We do this separately because sympy wants to treat my Psi above as immutatable on the diagonal for some reason
#So it is not letting me go through and redefine the diagonal entries, but it will let me add something to them
T = zeros(14,14)
i =0
while i < 7:
    T[i,i] = a
    T[i+7, i+7] = b
    i = i +1

Phi = Psi + T



