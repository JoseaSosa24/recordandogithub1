""" nombreUsuario = input("Digite su nombre: ")

# Casteo de datos (convertir un dato en otro)
edadUsuario = int(input("Digite su edad: "))

if edadUsuario > 18:
    print("Usted es mayor de edad")
else:
    print("Usted es menor de edad")

print("Usted no puede entrar a la disco") """

# hidroituango

nivelAgua = int(input("Cúal es el nivel de agua: ?"))

if nivelAgua > 0 and nivelAgua <= 200:
    print(f"El nivel de agua es: {nivelAgua},\n está muy bajo")
elif nivelAgua > 200 and nivelAgua <= 400:
    print(f"El nivel del agua es: {nivelAgua},\n estamos con normalidad")
elif nivelAgua > 400:
    print(f"el nivel de agua es: {nivelAgua}, inicie plan de evacuación")
else:
    print(f"Por favor revise el sensor de agua, nivel no valido")
