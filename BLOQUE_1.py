import math

#Se crea una clase circulo:
class Circulo:
    def __init__(self,radio):    #Se inicializa la clase con atributos
        self.radio = radio

    def area(self):                          #Se define el metodo para calculo del area
        return math.pi * (self.radio **2)
    
    def perimetro(self):                      #Se define el metodo para calculo del perimetro
        return 2 * math.pi * self.radio
    
    def diametro(self):                        #Se define el metodo para calculo del diametro
        return 2 * self.radio
    
#Se instancia dos circulos para la prueba

circ1=Circulo(5)          
circ2=Circulo(3)

print(circ2.area())
print(circ1.perimetro())
print(circ2.diametro())