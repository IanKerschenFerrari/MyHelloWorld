print("Iniciando... ")
from os import system
system("cls")
#Starting page
input("Pulse enter para continuar... ")
# CLS
from os import system
system("cls")
# Home page
print("__________________________________________________________Bienvenido________________________________________________________________")
print("Que desea hacer?")
print("Estas son las opciones...")
print('''1:Para explorar nuestra web prescione 1 y despues enter
2:Para usar la calculadora prescione 2 y despues enter
3:Para abrir alguna aplicacion prescione 3 y despues enter
4:Para jugar prescione 4 y despues enter''')
print("____________________________________________________________________________________________________________________________________")
app01 = input("Introdusca su numero aca: ")
# CLS
from os import system
system("cls")
# A few seconds
if app01 == ("1"):
    print("Ya se esta abriendo")

if app01 == ("2"):
    print('''Para realizar una suma prescione 1.
    para realizar una resta prescione 2.
    para realizar una multiplicacion prescione 3
    para realizar una diviscion prescione 4''')
    qqh = input('Pone tu numero aca: ')

if qqh == ("1"):
    suma1 = input("Que numero quieres sumar")
    suma2 = input("Que numero le quieres sumar")
    resulsum = int(suma1) + int(suma2)
    print(resulsum)
    input('Prescione enter para continuar')
if qqh == ("2"):
    resta1 = input("Que numero quieres restar")
    resta2 = input("Que numero quieres restarle")
    resulres = int(resta1) - int(resta2)
    print(resulres)
    input('Prescione una enter para continuar')
if qqh == ("3"):
    mul1 = input("Que numero quieres multiplicar")
    mul2 = input("Que numero quieres multiplicarle")
    resulmul = int(mul1) * int(mul2)
    print(resulmmul)
    input('Prescione una enter para continuar')
if qqh == ("4"):
    div1 = input("Que numero quieres dividir")
    div2 = input("Por que numero")
    resuldiv = int(div1) / int(div2)
    print(resuldiv)
    input('Prescione una enter para continuar')
if app01 == ("3"):
    print("Ya podras abrir tus applicaciones")
if app01 == ("4"):
    print("Ya podras Jugar")
# CLS
from os import system
system("cls")
# Abrir la app
print("____________________________________________________________|Os|___________________________________________________________________")
if app01 == ("1"):
    print('''Los temas que tenemos son:
    1:Autos
    2:Plantas
    3:Hardwere
    4:Recetas/Comidas
    5:#1 en Tendencias
    6:Sorteo''')
if app01 == ("2"):
    print("platas")
if app01 == ("3"):
    print('que aplicacion dwsea abrir')
if app01 == ("4"):
   print('''Los juegos disponibles son:
   1:TikTakToe
   2:El Orcado
   3:OS Game''')

else:
   print("Su comando no existe")