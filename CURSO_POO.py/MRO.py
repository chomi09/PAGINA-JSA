class F:
    def hablar(self):
        print('Hola desde F')

class A:
    def hablar(self):
        print('Hola desde A')

class B():
    def hablar(self):
        print('Hola desde B')
    
class C(A):
    def hablar(self):
        print('Hola desde C')
    
class D(F,C):
    def hablar(self):
        print('Hola desde D')
    
letrad = D()

print(D.mro())
letrad.hablar()
#B.hablar(letrad)