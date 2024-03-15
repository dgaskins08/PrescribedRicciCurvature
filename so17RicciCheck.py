from so17orthonormalbasis import *
from IntertwiningMap import *
from so17Ricci import *

#ric(.,.) should have a shape that matches the Phi. I should get 0's everwhere except along "diagonal" terms in the "four blocks"
#In terms of a (0,2) tensor this means that ric(e_i e_i) is non zero and ric(e_i e_i+7) = ric(e_i+7 e_i) is nonzero but zero elsewhere
#We also check bilinearity along the "off diagonal blocks"
#We also check scale invariance


#I ran the following code to check to make sure that it gave zeros where it should
i = 0
while i < 14:
    j = 0
    while j < 14:
        if i == j:
            pass
        else:
            if ric(PBasis1[i],PBasis1[j], Phi_inv, adpmat, PBasis1, PBasis2) == 0:
                pass
            else:
                print([i+1,j+1])
        j = j+1
    i = i +1
print("This checks out if you see [1, 8] , ..., [7, 14] and the same pairs swapped around since those correspond to the diagonal entries of the top right and bottom left blocks")

#Checking if the "top left block" is a multiple of the identity
i = 0
while i < 6:
    x = ric(PBasis1[i], PBasis1[i], Phi_inv, adpmat, PBasis1, PBasis2)
    y = ric(PBasis1[i+1], PBasis1[i+1], Phi_inv, adpmat, PBasis1, PBasis2)
    if x == y:
        pass
    else:
        print("uh oh")
        print([i, i+1])
    i = i +1
print("No uh oh? Success! The values representing the top left block entries are a multiple of the identity")
print("See an uh oh message? The pair [x,y] tells you which basis elements are the problem.")


#Checking if the "bottom right block" is a multiple of the identity
i = 7
while 6 < i < 13:
    x = ric(PBasis1[i], PBasis1[i], Phi_inv, adpmat, PBasis1, PBasis2)
    y = ric(PBasis1[i+1], PBasis1[i+1], Phi_inv, adpmat, PBasis1, PBasis2)
    if x == y:
        pass
    else:
        print("uh oh")
        print([i, i+1])
    i = i +1
print("No uh oh? Success! The values representing the bottom right block entries are a multiple of the identity")
print("See an uh oh message? The pair [x,y] tells you which basis elements are the problem.")

#Checking the "top right block" is a multiple of the idenity
i = 0
while i < 6:
    x = ric(PBasis1[i], PBasis1[i+7], Phi_inv, adpmat, PBasis1, PBasis2)
    y = ric(PBasis1[i+1], PBasis1[i+8], Phi_inv, adpmat, PBasis1, PBasis2)
    if x == y:
        pass
    else:
        print("uh oh")
        print([i, i+7])
    i = i +7
print("No uh oh? Success! The values representing the top right block entries are a multiple of the identity")
print("See an uh oh message? The pair [x,y] tells you which basis elements are the problem.")

#Check the "bottom left block" is a multiple of the identity
i = 0
while i < 6:
    x = ric(PBasis1[i+7], PBasis1[i], Phi_inv, adpmat, PBasis1, PBasis2)
    y = ric(PBasis1[i+8],PBasis1[i+1],  Phi_inv, adpmat, PBasis1, PBasis2)
    if x == y:
        pass
    else:
        print("uh oh")
        print([i, i+7])
    i = i +7
print("No uh oh? Success? The values representing the bottom left block entries are a multiple of the identity")
print("See an uh oh message? The pair [x,y] tells you which basis elements are the problem.")

#Checking symmetry of the "off diagonal blocks"
i = 0
while i < 6:
    x = ric(PBasis1[i], PBasis1[i+7], Phi_inv, adpmat, PBasis1, PBasis2)
    y = ric(PBasis1[i+7], PBasis1[i], Phi_inv, adpmat, PBasis1, PBasis2)
    if x == y:
        pass
    else:
        print("uh oh")
        print([i, i+1])
    i = i +1
print("No uh oh? Success! The top left block and bottom right block have the same diagonal entries")
print("See an uh oh message? The pair [x,y] tells you which basis elements are the problem.")


#Checking scale invariance
#Expect to get 3 zeros here
r1 = ric(PBasis1[0],PBasis1[0], Phi_inv, adpmat, PBasis1, PBasis2) - ric(PBasis1[0],PBasis1[0], d*Phi_inv, adpmat, PBasis1, PBasis2)
r2 = ric(PBasis1[8],PBasis1[8], Phi_inv, adpmat, PBasis1, PBasis2) - ric(PBasis1[8],PBasis1[8], d*Phi_inv, adpmat, PBasis1, PBasis2)
r3 = ric(PBasis1[0],PBasis1[7], Phi_inv, adpmat, PBasis1, PBasis2) - ric(PBasis1[0],PBasis1[7], d*Phi_inv, adpmat, PBasis1, PBasis2)

print("Do you see three zeros below? If so, success! ric is scale invariant. Otherwise, the nonzero term corresponds to a not scale invariant value")
r1 = simplify(r1)
print_latex(r1)
r2 = simplify(r2)
print_latex(r2)
r3 = simplify(r3)
print_latex(r3)