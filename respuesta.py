def ejercicio1():
    print("hello world")

def ejercicio2(a,b,c):
    if isinstance(a, int) and isinstance(b, str) and isinstance(c, float):
        print(f"{a}\n{b}\{c}")
    else:
        print("error")
def ejercicio3(a,b):
    print(int(a) + int(b))

def ejercicio4(a, b):
    print(float(a) + float(b))

def ejercicio5(a,b,c,d,e):
    resultado = ""
    for i in [a,b,c,d,e][:-1]:
        resultado += i+ "," 
    else:
        resultado += e
    print(resultado)

def ejercicio5(a,b,c,d,e):
    resultado = ""
    for i in [a,b,c,d,e][::-1]:
        resultado += i+ "," 
    else:
        resultado += a
    print(resultado)

def ejercicio6(a,b,c,d,e):
    print(f"{a + b + c + d + e}\n{e + d + c + b + a}")

def ejercicio7(a,b):
    print(f"La suma de operador1 y operador2 es: {a + b}")
    print(f"La resta de operador1 y operador2 es: {a - b}")
    print(f"La multiplicación de operador1 y operador2 es: {a * b}")
    print(f"La división de operador1 y operador2 es: {round(a / b, 2)}")
    print(f"El exponente de operador1 y operador2 es: {a ** b}")
    print(f"La división entera de operador1 y operador2 es: {a // b}")

def ejercicio8(a):
    print(f"el número de minutos es: {} y en segundos es: {}")