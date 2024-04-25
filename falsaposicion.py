import math

def falsa_posicion(f, a, b, tol=1e-6, max_iter=100):
    
    iteraciones = []
    
    iter_count = 0
    while iter_count < max_iter:
        fa = f(a)
        fb = f(b)    
        # Verificar si la función tiene signos opuestos en los límites
        if fa * fb > 0:
            raise ValueError("La función debe tener signos opuestos en los límites del intervalo.")
        
        # Cálculo del nuevo punto c
        c = b - ((fb * (b - a)) / (fb - fa))
        fc = f(c)
        
        # Añadir datos a la tabla de iteraciones
        iteraciones.append([
            iter_count + 1,  
            a,  
            b,  
            fa,  
            fb,  
            c,  
            fc   
        ])
        
        # Si la tolerancia es menor que el umbral, hemos encontrado la raíz
        if abs(fc) < tol:
            return iteraciones
        
        # Reasignar el intervalo basado en el signo del producto fa*fc
        if fa * fc < 0:
            b = c
        else:
            a = c
        
        iter_count += 1
    
    print("El método no convergió después de", max_iter, "iteraciones.")
    return iteraciones


try:
    # Pedir la definición de la función
    funcion_str = input("Ingrese la función f(x) en formato (ejemplo: x**3 - 2*x + 1'): ")
    
    if not funcion_str.startswith("lambda"):
        funcion_str = "lambda x: " + funcion_str
    
    funcion = eval(funcion_str)

    a = float(input("Ingrese el límite inferior del intervalo (a): "))
    b = float(input("Ingrese el límite superior del intervalo (b): "))
    
    tolerancia = float(input("Ingrese la tolerancia (o presione Enter para usar 1e-6): ") or 1e-6)

    iteraciones = falsa_posicion(funcion, a, b, tol=tolerancia)

    # Imprimir la tabla de iteraciones con formato alineado y 6 decimales
    print("Tabla de iteraciones:")
    print("Iteración\t      A\t      B\t   f(A)\t   f(B)\t      Xi\t   f(Xi)")
    
    for iteracion in iteraciones:
        fila = [f"{iteracion[0]:6d}"] + [f"{x:10.6f}" for x in iteracion[1:]]
        print("\t".join(fila))

    raiz_aproximada = iteraciones[-1][5]
    print(f"\nLa raíz aproximada es: {raiz_aproximada:.6f}")

except ValueError as ve:
    print("Error:", ve)

except SyntaxError:
    print("Error en la definición de la función. Por favor, asegúrate de usar el formato correcto.")

except Exception as e:
    print("Error inesperado:", e)