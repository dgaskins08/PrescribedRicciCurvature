from so17orthonormalbasis import *
from IntertwiningMap import *

#This is the collection of 14x14 matrices for adg2 acting on p_1 + p_2
#There are 14 entries as is checked here
admat
print("The number of adg2 maps is ", len(admat))
print("Was it 14? If so, success! If not... oops")


#This is the intertwining map on p_1 + p_2
Phi


#This checks to make sure that the Phi intertwines.
#It fails if you get "uh oh" and it tells you which element it fails for
i = 0
for x in admat:
    if Phi*x - x*Phi == zeros(14,14):
        pass
    else:
        print("uh oh")
        print(x)
print("if no uh oh, then success! Phi is an intertwining map!")