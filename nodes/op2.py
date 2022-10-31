from .nodes import *

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')
I = Node('I')
J = Node('J')
K = Node('K')

A.connect(B, 17)
A.connect(J, 52)

B.connect(C, 14)
B.connect(F, 69)
B.connect(K, 44)

C.connect(D, 25)
C.connect(I, 32)

D.connect(E, 100)
D.connect(I, 13)

E.connect(F, 8)
E.connect(K, 18)

F.connect(G, 2)

G.connect(H, 40)

H.connect(I, 27)

J.connect(K, 72)

result_table = ResultNodeTable()

result_table.A = ResultNode(A)
result_table.B = ResultNode(B)
result_table.C = ResultNode(C)
result_table.D = ResultNode(D)
result_table.E = ResultNode(E)
result_table.F = ResultNode(F)
result_table.G = ResultNode(G)
result_table.H = ResultNode(H)
result_table.I = ResultNode(I)
result_table.J = ResultNode(J)
result_table.K = ResultNode(K)