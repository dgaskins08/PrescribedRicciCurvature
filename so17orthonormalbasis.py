from sympy import *
from sympy import Matrix
from sympy.abc import a, b,c,d

def bracket(a,b):
    return (a*b - b*a)

def printbasistolatex(Basis):
    i = 1
    for x in Basis:
        print(i)
        print_latex(x)
        print("\\" "\\")
        i = i+1

#This is G2 as given by Maple a subalgebra of so(7). I was able to tell Maple to copy to python code and then I pasted it here
G2 = [Matrix([[0,1,0,0,0,0,0],[-1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,-1,0,0],[0,0,0,0,0,0,0]]), Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,-1,0,0],[0,0,0,-1,0,0,0]]),Matrix([[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,0,0],[0,0,0,0,-1,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,-1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,-1,0]]),Matrix([[0,0,0,0,0,0,1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,-1,0,0,0,0,0]]),Matrix([[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,-1,0],[-1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,1,0,0],[0,-1,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,-1,0,0,0],[0,0,0,0,0,0,1],[0,0,0,0,0,-1,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,-1],[0,0,0,-1,0,0,0],[0,0,0,0,1,0,0]]),Matrix([[0,0,0,0,1,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,1,0,0],[0,0,0,-1,0,0,0],[0,0,1,0,0,0,0],[0,-1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,1,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,-1,0,0,0,0],[0,0,0,0,0,0,0],[-1,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,1,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,-1,0,0,0,0,0],[0,0,1,0,0,0,0]])]

#This is so(7) as given by Maple. I copied as python code again and pasted here. I don't  like its presentation, and I want each element's negative
so7 = [Matrix([[0,-1,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]), Matrix([[0,0,-1,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,-1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]), Matrix([[0,0,0,0,-1,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,-1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[1,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,-1,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,-1,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,-1,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,-1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,1,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,-1,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,-1,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,-1,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,1,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,-1,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0]]), Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,-1,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,1,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,-1,0],[0,0,0,0,1,0,0],[0,0,0,0,0,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,0,0],[0,0,0,0,1,0,0]]),Matrix([[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,0],[0,0,0,0,0,0,-1],[0,0,0,0,0,1,0]])]
Newso7 = []
for x in so7:
    Newso7 = Newso7 + [-x]



#The G2 basis we have is not orthogonal under trace pairing, and we ultimately want it's orthogonal complement
#The approach is to us gram-schmidt on G2 with the trace pairing
#We then get a linearly independent complement of G2 in so(7) and gram-schmidt the orthogonal basis for G2 with the lin. ind. complement

#First we defined a metric of so(7), the scalar is chosen to make things look nicer
def metric(u,v):
    return(-S(6)*trace(u*v))

#This defines the projection of v onto u using the metric we defined. This is needed for gram-schmidt
def proj(u,v):
    return((S(metric(u,v))/metric(u,u))*u)

#This defines the gram-schmidt procedure function. It needs a basis, the dimension of the basis, and the size the sqaure matrices
#This function returns an orthonormal basis
def gramschmidt(Basis, Dim, n):
    NewBasis = [S(1)/(sqrt(metric(Basis[0], Basis[0])))*Basis[0]]
    i = 1
    j = 0
    Sub = zeros(n, n)
    while i < Dim:
        while j < i:
            Sub = Sub + proj(NewBasis[j], Basis[i])
            j = j + 1
        E = Basis[i] - Sub
        E = (S(1)/(sqrt(metric(E,E))))*E
        i = i+1
        NewBasis = NewBasis + [E]
        j = 0
        Sub = zeros(n,n)
    return(NewBasis)




#This is to get my orthonormal G2
NewG2 = gramschmidt(G2, 14, 7)


#Below is a Linearly independent complement to G2 in so(7)
#The process to achieve this was to look at the original G2 write out the elements as basis elements of so(7)
#There was an obvious choice once you write out the origial G2 elements
K1 = Newso7[0] + Newso7[17]
K2 = Newso7[2] - Newso7[10]
K3 = Newso7[4] - Newso7[8]
K4 = Newso7[1] - Newso7[16]
K5 = Newso7[3] + Newso7[9]
K6 = Newso7[5] + Newso7[7]
K7 = Newso7[6] + Newso7[15]
LIC = [K1, K2, K3, K4, K5, K6, K7]

TheBasis = NewG2 + LIC

#This will provide a basis for the p_1 in so(7) and should keep the basis for G2 the same
TheNewBasis = gramschmidt(TheBasis, 21, 7)


#We now have an orthonormal g2 and we have an orthonormal basis for an invariant complement


#We now want to place our basis for so(7) inside so(1,7)
#This will only require adding a column and row of zeros to the left and top


so17Basis1 = []
for x in TheNewBasis:
    row = zeros(1, 7)
    col = zeros(8, 1)
    R = x.row_insert(0, row)
    C = R.col_insert(0, col)
    so17Basis1 = so17Basis1 + [C]


#I now want to create a basis that uses the original basis given for g2 to avoid any concern about the new g2 basis not being g2

#Placing the original g2 basis in so(1,7) which doesn't change bracket relations or dimension
G28 = []
for x in G2:
    row = zeros(1, 7)
    col = zeros(8, 1)
    R = x.row_insert(0, row)
    C = R.col_insert(0, col)
    G28 = G28 + [C]


#Now we need our p_2 and to complete our so17Basis that is orthonormal
#There is an obvious choice for a basis of p_2 to make
#We will have to rescale our basis in p_2 piece to ensure that this basis is not just orthogonal but orthonormal for our metric

#These are matrices with ones along the first row except the diagonal and 0's elsewhere
e1 = Matrix([[0,1, 0,0,0,0,0,0], zeros(7,8)])
e2 = Matrix([[0,0, 1,0,0,0,0,0], zeros(7,8)])
e3 = Matrix([[0,0, 0,1,0,0,0,0], zeros(7,8)])
e4 = Matrix([[0,0, 0,0,1,0,0,0], zeros(7,8)])
e5 = Matrix([[0,0, 0,0,0, 1,0,0], zeros(7,8)])
e6 = Matrix([[0,0, 0,0,0, 0,1,0], zeros(7,8)])
e7 = Matrix([[0,0, 0,0,0, 0,0, 1], zeros(7,8)])


p1 = e1 + transpose(e1)
p2 = e2 + transpose(e2)
p3 = e3 + transpose(e3)
p4 = e4 + transpose(e4)
p5 = e5 + transpose(e5)
p6 = e6 + transpose(e6)
p7 = e7 + transpose(e7)


P = [p1, p2, p3, p4, p5, p6, p7]







so17Basis = G28 + so17Basis1[14:21] + P
#printbasistolatex(so17Basis)

#I now want to reorder the basis in p_1 to get the intertwing map to be diagonal in all four blocks, and in addition to this
#We will rescale the basis in p_2 so that it is orthonormal

A = so17Basis[0:14]
B = [so17Basis[20], -so17Basis[17], so17Basis[14], -so17Basis[18], so17Basis[15], so17Basis[19], -so17Basis[16]]
C = []
for x in so17Basis[21:28]:
    y = S(1)/sqrt(12)*x
    C = C + [y]
so17Basis = A + B + C




#The following assignments are in some sense redundant, but it puts a nice name on them

#G2 in so(1,7)
G28 = so17Basis[0:14]

#p_1
P1 = so17Basis[14:21]

#p_2
P2 = so17Basis[21:28]


#Here is the metric to make so17Basis orthonormal. P2 is the only not orthonormal piece left
#It is important to recognize that this metric works fine on P2 so long as it is an elemnt of P1, the collection of basis elements
#However, if you try to use the metric on a linear combination of basis elements in P2, it will not work
#The purpose of defining the metric this way is to make it simple for checking orthonormality of the basis
def metric1(u,v):
    if u in P2 and v in P2:
        return(S(6)*trace(u*v))
    else:
        return(metric(u,v))

printbasistolatex(P1)
printbasistolatex(P2)