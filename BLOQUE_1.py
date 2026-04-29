import math

#Ejercicio 1.1
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

#Ejercicio 1.2
# Se crea la clase cuenta bancaria

class CuentaBancaria:

    def __init__(self,titular,saldo):
        self.titular = titular
        self._saldo = saldo    #Se usa el pilar de POO encapsulamiento

    def depositar(self,monto):
        self._saldo += monto
        return f"Se deposito a la cuenta: ${monto}.Total saldo:$ {self._saldo}"

    def extraer(self, monto):
        if monto > self._saldo:
            return "Saldo insuficiente,ingrese otro monto"
        else:
             self._saldo - monto
             return f"¡Operacion exitosa!. Su saldo actual es: ${self._saldo}"
    
    def consultar_saldo(self):
        return f"Su saldo actual es de: ${self._saldo}"
    
cuenta1=CuentaBancaria("Juan Perez",1000)
cuenta2=CuentaBancaria("Juana Paz", 50000)

print(cuenta1.titular)
print(cuenta2.depositar(10000))
print(cuenta1.extraer(2000))
print(cuenta2.consultar_saldo())
