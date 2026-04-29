#Ejercicio 2.1
import math
#Creacion de clase padre figura:

class Figura :

    def area(self):
        raise NotImplementedError

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado= lado

    def area(self):
        return self.lado * self.lado


class Triangulo(Figura):
    def __init__(self, base, altura):
        self.base= base
        self.altura= altura

    def area(self):
        return (self.base * self.altura) / 2
      

class Circulo(Figura):
    def __init__(self, radio):
        self.radio= radio

    def area(self):
        return math.pi * (self.radio ** 2)
    

figuras= [Cuadrado(6), Triangulo(3,6), Circulo(3)]

for f in figuras:
    print(f"El area de la figura es:{f.area()}")
    
