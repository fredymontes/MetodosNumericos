import math

def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) > 0:
        print("La función no cumple con el teorema del valor intermedio en el intervalo dado.")
        return None

    iter_count = 0
    result = None
    error = None

    print("Iteración | (Xi) Inferior | (Xs) Superior |     Xa     |    F(xi)   |    F(xa)   | f(xi)*f(xa) | Cambio | Error f(Xa)")
    print("-------------------------------------------------------------------------------------------------------------------")
    
    while iter_count < max_iter:
        xa = (a + b) / 2
        fxa = func(xa)
        fa = func(a)
        cambio = "Xi" if fa * fxa < 0 else "Xs"
        error = abs(xa - a)
        
        print(f"{iter_count+1: ^9} | {a: ^13.6f} | {b: ^13.6f} | {xa: ^10.6f} | {fa: ^10.6f} | {fxa: ^10.6f} | {fa*fxa: ^12.6f} | {cambio: ^6} | {error: ^12.6f}")
        
        if error < tol:
            result = xa
            break

        if fa * fxa < 0:
            b = xa
        else:
            a = xa

        iter_count += 1

    return result

# Solicitar al usuario ingresar la función
funcion_input = input("Ingrese la función (por ejemplo, '2*x**2 - 10*x + 3'): ")
def funcion(x):
    return eval(funcion_input)

# Solicitar al usuario ingresar el intervalo de inicio
a = float(input("Ingrese el límite inferior del intervalo: "))
b = float(input("Ingrese el límite superior del intervalo: "))

resultado = bisection_method(funcion, a, b)
print("\nLa raíz aproximada es:", resultado)