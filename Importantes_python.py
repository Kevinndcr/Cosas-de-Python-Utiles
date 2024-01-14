import os #libreria para utilizar distintos comandos del sistema operativo
import time #libreria para utilizar unas cuestiones de tiempo (en este codigo para hacer un freeze al codigo xd)

class Celular:
    def __init__(self, marca, modelo, lanzamiento):
        self.marca = marca
        self.modelo = modelo
        self.lanzamiento = lanzamiento

celulares = []

def agregaCelulares(marca, modelo, lanzamiento):
    nuevo_celular = Celular(marca, modelo, lanzamiento)
    celulares.append(nuevo_celular)
    print('Se ha agreado el celular exitosamente. \n')

def mostrarCelulares(celulares):
    print('Celulares registrados en la lista:\n')
    for celular in celulares:
        print(f' Marca: {celular.marca}\n Modelo: {celular.modelo}\n Año Lanzamiento: {celular.lanzamiento}\n')

#imprimiendo solo modelos
def buscaModelo(model, celulares):
    for pos_celular, nom_modelo in enumerate(celulares):
        if model == nom_modelo.modelo:
            #print(f"Se encontro en la pos {pos_celular}") # dato xd
            return pos_celular

    #print('no se encontro xd') #dato pt 2 xd
    return -1 
    
def datos_modelo_especifico(pos, celulares):
    print()
    print("Datos del modelo en especifico:\n")
    print(f'Marca: {celulares[pos].marca} \nModelo: {celulares[pos].modelo} \nLanzamiento: {celulares[pos].lanzamiento}')

#inicializando algunos random
agregaCelulares('Apple', 'Iphone 8', '2014')
agregaCelulares('Samsung', 'Samsung Galaxy S23', '2022')

#1. Mostrar celulares en la lista
#2. Agregar Celular
#3. Buscar telefono especifico (por modelo) y dar esa info
#4. Salir

print('Hola! Bienvenido a esta prueba de listas y objetos!')

while True:
    opc = int(input(""" 
    1. Mostrar Celulares en la lista
    2. Agregar un Celular a la lista
    3. Buscar modelo especifico
    4. Salir
                    
    Digite su opcion: """))
    
    os.system('cls') #esto es un limpiar pantalla
    print('')

    if opc == 1:
        mostrarCelulares(celulares)
    elif opc == 2:
        marca_celular = input("Digite la marca de su celular: ")
        modelo_celular = input("Digite el modelo del celular: ")
        lanzamiento_celular = input("Ingrese anho de lanzamiento: ")
        nuevo_celular = Celular(marca_celular, modelo_celular, lanzamiento_celular)
        celulares.append(nuevo_celular)
    
    elif opc == 3:
        modelo_a_buscar = input("\nDigite el modelo del telefono que desea buscar: ")
        verificador = buscaModelo(modelo_a_buscar, celulares) #guarda ya sea la pos donde encontro o un False
        if verificador != -1:
            datos_modelo_especifico(verificador, celulares)
        else:
            print('\nNo se ha encontrado el modelo que desea buscar.')
    elif opc == 4:
        os.system('cls')
        for animation in range (1, 3):
            print("""
            /\_/\ 
            ( o.o ) 
            > ^ <  
            Adiós!
            """)
            time.sleep(1)
            os.system('cls')

            print("""
            /\_/\ 
            ( -.- ) 
            > ^ <  
            Hasta luego!
            """)
            time.sleep(1)
            os.system('cls')
        
            print("""
            /\_/\ 
            ( T.T ) 
            > ^ <  
            Nos vemos!
             """)
            time.sleep(1)
            os.system('cls')
        break;


print("""
                            /\_/\ 
                            ( 0.0 ) __,_____
                            >   >  / __.==--"        
                                  /#(-'      
                                  `-'
          
                            Te jodiste
""")
    




