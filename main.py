from BLOQUE_2 import Perro, Gato, Vaca, Pato, Oveja

animales= [
    Perro("Mavis", 4),
    Gato("Gary", 5),
    Vaca("Lola", 4), 
    Pato("Patricio", 2),
    Oveja("Oscar",3)
    ]
for a in animales:
    print(f"{a.get_nombre()} ({a.get_edad()} años) dice: {a.hablar()}")