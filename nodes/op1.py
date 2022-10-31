from .nodes import *

A = Node('A')
B = Node('B')
C = Node('C')
D = Node('D')
E = Node('E')
F = Node('F')
G = Node('G')
H = Node('H')

A.connect(B, 4)
A.connect(C, 2)

B.connect(C, 2)
B.connect(D, 1)

C.connect(E, 6)

D.connect(E, 2)
D.connect(F, 6)
D.connect(G, 5)

E.connect(F, 4)
E.connect(G, 5)

F.connect(G, 10)
F.connect(H, 8)

G.connect(H, 12)

result_table = ResultNodeTable()

result_table.A = ResultNode(A)
result_table.B = ResultNode(B)
result_table.C = ResultNode(C)
result_table.D = ResultNode(D)
result_table.E = ResultNode(E)
result_table.F = ResultNode(F)
result_table.G = ResultNode(G)
result_table.H = ResultNode(H)