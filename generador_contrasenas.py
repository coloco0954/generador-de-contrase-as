#Generador contraseñas

#Hacemos las importaciones
import random
import string

letras = string.ascii_letters #guardamos todas las letras del abecedario
numeros = string.digits #guardamos todos los numero (del 0 al 9)

longitud_contrasena = random.randint(10,20) #Definimos de manera aleatoria la longitud de la contraseña

#con random.choice decimos que de la suma o concatenacion de letras y numeros nos muestre uno de esos caracteres de manera aleatoria y con bucle for definimos las veces
#que se mostraran esos caracteres, en un rango de 0 a longitud_contrasena que eso lo definimos en la variable, y con .join simplemente agregamos el resultado al string
contrasena = ''.join(random.choice(letras + numeros) for _ in range(longitud_contrasena)) 

#imprimimos la contraseña
print(contrasena)