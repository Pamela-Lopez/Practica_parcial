#Desarrollo de ejercicio 3.1
class Procesador:
    def __init__(self,modelo):
        self.modelo = modelo
        
        

class Memoria:
    def __init__(self,capacidad):
        self.capacidad = capacidad


class Computadora:
    def __init__(self, marca, modelo_cpu, ram):
        self.marca = marca
        # Se crean ADENTRO: esto es lo que define la composición
        self.procesador = Procesador(modelo_cpu)
        self.memoria = Memoria(ram)

    def ficha_tecnica(self):
        print(f"Computadora {self.marca}:")
        print(f"- {self.procesador}")
        print(f"- {self.memoria}")

# Uso
c = Computadora("Asus", "Intel i5", 16)
c.ficha_tecnica()


#Ejercicio 3.2

class Cancion:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor

class Playlist:
    def __init__(self,nombre):
        self.nombre = nombre
        self.canciones = []  
        
    def agregar_cancion(self,c):
        self.canciones.append(c)
        
    def  cantidad(self):
        return len(self.canciones)
        
    def listar(self):
        print(f"--- Playlist: {self.nombre} ---")
        for c in self.canciones:
            print(f"- {c.titulo} ({c.autor})")

c1 = Cancion("Bohemian Rhapsody", "Queen")
c2 = Cancion("Yellow Submarine", "The Beatles")

# 2. Creamos la Playlist y le agregamos las canciones
mi_lista = Playlist("Favoritos")
mi_lista.agregar_cancion(c1)
mi_lista.agregar_cancion(c2)

# 3. Probamos los métodos
mi_lista.listar()
print(f"Total de canciones: {mi_lista.cantidad()}")
        

