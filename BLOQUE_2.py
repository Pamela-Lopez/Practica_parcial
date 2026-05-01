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
    print(f"El área de la figura es:{f.area()}")




#Ejercicio 2.2

class Animal:
    def __init__(self, nombre, edad):
        self._nombre = nombre # encapsulamiento (convención con guion bajo)
        self._edad = edad
    def get_nombre(self): # getter
        return self._nombre
    def get_edad(self):
        return self._edad
    def hablar(self): # abstracción: las hijas la implementan
        raise NotImplementedError("Las subclases deben implementar hablar()")

class Perro(Animal): # herencia
    def hablar(self): # polimorfismo (override)
        return "Guau!"

class Gato(Animal):
    def hablar(self):
        return "Miau!"

class Vaca(Animal):
    def hablar(self):
        return "Muu!"
    
class Pato(Animal):
    def hablar(self):
        return "Cuack Cuack!"
    
class Oveja(Animal):
    def hablar(self):
        return "Meee!"


    
