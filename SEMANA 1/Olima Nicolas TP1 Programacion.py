#   1) Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”.
print("EJERCICIO 1")

print("Hola mundo!")

print() #   salto de línea

#   2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando
#   el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir
#   por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para
#   realizar la impresión por pantalla.
print("EJERCICIO 2")

nombre=input("Por favor ingrese su nombre: ")
print(f"Hola {nombre}!!")

print() #   salto de línea

#   3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e
#   imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa
#   “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30
#   años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar
#   la impresión por pantalla.
print("EJERCICIO 3")

nombre=input("Por favor ingrese su nombre: ")
apellido=input("Por favor ingrese su apellido: ")
edad=input("Por favor ingrese su edad: ")
lugar=input("Por favor ingrese su lugar de residencia: ")

print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

print() #   salto de línea

#   4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#   su perímetro.

print("EJERCICIO 4")

pi=3.14159
radio=float(input("Ingrese el radio de un círculo: "))
area= pi*radio*radio
perimetro= 2*pi*radio

print(f"Area del círculo de radio {radio}: {area:.2f}")
print(f"Perímetro del círculo de radio {radio}: {perimetro:.2f}")

print() #   salto de línea

#   5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a
#   cuántas horas equivale.

print("EJERCICIO 5")

segs=int(input("Ingrese segundos: "))
print(f"Equivale a {segs/3600} horas.")

print() #   salto de línea

#   6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#   multiplicar de dicho número.

print("EJERCICIO 6")

num=int(input("Ingrese un número: "))
for i in range(1,11):
    print(f"{num}x{i} = {num*i}")

print() #   salto de línea

#   7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por
#   pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

print("EJERCICIO 7")

num1=int(input("Ingrese el primer número entero: "))
num2=int(input("Ingrese el segundo número entero: "))

print(f"{num1} + {num2} = {num1+num2}")
print(f"{num1} - {num2} = {num1-num2}")
print(f"{num1} * {num2} = {num1*num2}")
print(f"{num1} / {num2} = {num1/num2}")

print() #   salto de línea

#   8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice
#   de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente
#   modo:
#   𝐼𝑀𝐶 =   𝑝𝑒𝑠𝑜 𝑒𝑛 𝑘𝑔 /((𝑎𝑙𝑡𝑢𝑟𝑎 𝑒𝑛 𝑚)^2)"

print("EJERCICIO 8")

alt=float(input("Ingrese su altura: "))
peso=float(input("Ingrese su peso: "))
imc=peso/(alt**2)

print(f"IMC= {imc:.2f}")

print() #   salto de línea

#   9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por
#   pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia:
#   𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐹𝑎ℎ𝑟𝑒𝑛ℎ𝑒𝑖𝑡 =9/5 . 𝑇𝑒𝑚𝑝𝑒𝑟𝑎𝑡𝑢𝑟𝑎 𝑒𝑛 𝐶𝑒𝑙𝑠𝑖𝑢𝑠 + 32

print("EJERCICIO 9")

t=float(input("Ingrese temperatura en celsius: "))
f= 9/5* t +32

print(f"{t:.0f}°C = {f:.0f}°F")

print() #   salto de línea

#   10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de
#   dichos números.

print("EJERCICIO 10")

n1=float(input("Ingrese el primer número: "))
n2=float(input("Ingrese el segundo número: "))
n3=float(input("Ingrese el tercer número: "))

print(f"PROMEDIO= {(n1+n2+n3)/3}")

print() #   salto de línea

#   prueba git