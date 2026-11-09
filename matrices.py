# Ejercicio 1: análisis de una matriz de ventas
# Filas = vendedores, columnas = semanas (ventas en millones de pesos)

ventas = [
    [12, 15, 10, 18],
    [8, 14, 16, 12],
    [20, 18, 15, 22]
]


def mostrar_matriz(matriz):
    print("\n1. MATRIZ DE VENTAS (millones de pesos)")
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            print(f"Vendedor {i + 1}, Semana {j + 1}: {matriz[i][j]}")


def total_por_vendedor(matriz):
    print("\n2. TOTAL POR VENDEDOR")
    totales = []
    for i in range(len(matriz)):
        suma = 0
        for valor in matriz[i]:
            suma += valor
        totales.append(suma)
        print(f"Vendedor {i + 1}: {suma}")
    return totales


def total_por_semana(matriz):
    print("\n3. TOTAL POR SEMANA")
    totales = []
    for j in range(len(matriz[0])):
        suma = 0
        for i in range(len(matriz)):
            suma += matriz[i][j]
        totales.append(suma)
        print(f"Semana {j + 1}: {suma}")
    return totales


def mayor_vendedor(totales):
    mayor = totales[0]
    posicion = 0
    for i in range(len(totales)):
        if totales[i] > mayor:
            mayor = totales[i]
            posicion = i
    print(f"\n4. Mejor vendedor: Vendedor {posicion + 1} con {mayor} millones")


def mayor_semana(totales):
    mayor = totales[0]
    posicion = 0
    for j in range(len(totales)):
        if totales[j] > mayor:
            mayor = totales[j]
            posicion = j
    print(f"5. Mejor semana: Semana {posicion + 1} con {mayor} millones")


def promedio_general(matriz):
    suma = 0
    cantidad = 0
    for fila in matriz:
        for valor in fila:
            suma += valor
            cantidad += 1
    print(f"6. Promedio general de ventas: {suma / cantidad:.2f} millones")


def modificar_venta(matriz):
    print("\n7. MODIFICAR UNA VENTA")
    vendedor = int(input("Número de vendedor (1-3): "))
    semana = int(input("Número de semana (1-4): "))

    if 1 <= vendedor <= len(matriz) and 1 <= semana <= len(matriz[0]):
        nuevo = float(input("Nuevo valor de ventas: "))
        matriz[vendedor - 1][semana - 1] = nuevo
        print("Venta actualizada.")
    else:
        print("Posición inválida.")


def mostrar_resultados(matriz):
    mostrar_matriz(matriz)
    totales_v = total_por_vendedor(matriz)
    totales_s = total_por_semana(matriz)
    mayor_vendedor(totales_v)
    mayor_semana(totales_s)
    promedio_general(matriz)


# Programa principal
print("===== RESULTADOS INICIALES =====")
mostrar_resultados(ventas)

modificar_venta(ventas)

print("\n===== RESULTADOS ACTUALIZADOS =====")
mostrar_resultados(ventas)


# Ejercicio 2: participación en cursos con conjuntos (set)

curso_A = {
    "Ana", "Carlos", "Laura", "Pedro",
    "Sofia", "Andres", "Camila"
}

curso_B = {
    "Laura", "Pedro", "Daniel", "Sofia",
    "Mateo", "Valentina"
}


def mostrar_analisis(a, b):
    print("\n1. Estudiantes del curso A:", a)
    print("   Estudiantes del curso B:", b)
    print("2. Estudiantes diferentes en total:", len(a | b))
    print("3. Inscritos en ambos cursos:", a & b)
    print("4. Solo en el curso A:", a - b)
    print("5. Solo en el curso B:", b - a)
    print("6. Inscritos en exactamente uno de los dos:", a ^ b)
    print("7. ¿Todos los del curso A están también en B?", a <= b)


def agregar_estudiante():
    curso = input("\n¿A qué curso desea agregar? (A/B): ").upper()
    nombre = input("Nombre del estudiante: ").strip().capitalize()

    if curso == "A":
        curso_A.add(nombre)
        print(f"{nombre} agregado al curso A.")
    elif curso == "B":
        curso_B.add(nombre)
        print(f"{nombre} agregado al curso B.")
    else:
        print("Curso inválido.")


# Programa principal
print("===== RESULTADOS INICIALES =====")
mostrar_analisis(curso_A, curso_B)

agregar_estudiante()

print("\n===== RESULTADOS ACTUALIZADOS =====")
mostrar_analisis(curso_A, curso_B)
