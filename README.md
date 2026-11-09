# Taller_8_Matrices

# Taller 8: Matrices y Conjuntos en Python

Lógica de Programación - Almacenamiento y manipulación de información

**Autor:** Joan Nicolas Rey Gomez

## Contenido del repositorio

| Archivo | Descripción |
|---|---|
| `ejercicio1_matriz.py` | Análisis de una matriz de ventas (3 vendedores x 4 semanas) |
| `ejercicio2_conjuntos.py` | Análisis de participación en cursos usando conjuntos (`set`) |

## Cómo ejecutar

```bash
python ejercicio1_matriz.py
python ejercicio2_conjuntos.py
```

No se usan librerías externas (sin NumPy).

---

## Ejercicio 1: Matriz de ventas

### Procedimiento

La información se guardó en una lista de listas, donde cada fila representa un vendedor y cada columna una semana. Se usaron ciclos `for` anidados y acumuladores (`suma += valor`) para calcular el total por vendedor (recorriendo filas) y el total por semana (recorriendo columnas). Para encontrar el mayor valor se guardó el primer total como referencia y se comparó con los demás. El promedio general se calculó dividiendo la suma de todos los elementos entre la cantidad de elementos. Por último, el programa pide la posición y el nuevo valor para modificar la matriz y vuelve a mostrar todos los resultados.

### Preguntas de análisis

**1. ¿Por qué resulta conveniente utilizar una matriz en lugar de cuatro listas independientes?**

Porque una matriz agrupa todos los datos en una sola estructura organizada en filas y columnas, y cada dato se ubica con dos índices (vendedor y semana). Esto permite recorrer toda la información con ciclos anidados y escribir el código una sola vez. Además, el programa funciona igual si aumenta el número de vendedores o de semanas. Con cuatro listas independientes habría que repetir el código para cada una, sería más difícil relacionar los datos de un mismo vendedor y habría más riesgo de errores.

**2. ¿Qué diferencia existe entre recorrer una fila y recorrer una columna?**

Al recorrer una **fila** se deja fijo el índice de la fila y se mueve el de la columna (`matriz[i][j]` con `i` fijo). En este problema equivale a ver todas las ventas de un mismo vendedor en las cuatro semanas. Al recorrer una **columna** se deja fijo el índice de la columna y se mueve el de la fila (`j` fijo). Equivale a ver las ventas de los tres vendedores en una misma semana. Recorrer filas es directo con `for fila in matriz`, mientras que recorrer columnas requiere usar los índices.

**3. ¿Qué sucede si se modifica un elemento de la matriz? ¿Cómo afecta esto a los resultados?**

Cambia únicamente el valor de esa posición, pero como todos los resultados se calculan con ciclos cada vez que se ejecuta el análisis, se actualizan automáticamente: el total del vendedor, el total de la semana y el promedio general cambian, y también pueden cambiar el mejor vendedor y la mejor semana si el nuevo valor altera el orden. Por eso no se deben escribir los resultados a mano: el programa siempre refleja los datos actuales.

---

## Ejercicio 2: Participación en cursos

### Procedimiento

Los estudiantes de cada curso se guardaron en conjuntos (`set`), que no permiten elementos repetidos. Las operaciones se resolvieron con los operadores de conjuntos de Python: unión (`|`) para contar estudiantes diferentes, intersección (`&`) para los que están en ambos cursos, diferencia (`-`) para los que están solo en uno, diferencia simétrica (`^`) para los que están en exactamente uno de los dos, y subconjunto (`<=`) para saber si todos los del curso A están en el B. Para agregar un estudiante se usó el método `.add()` y luego se volvió a ejecutar el análisis con los datos actualizados. Cada resultado se muestra con un mensaje descriptivo.

### Preguntas de análisis

**1. ¿Por qué un conjunto es más apropiado que una lista para representar estudiantes inscritos sin duplicados?**

Porque el conjunto elimina los duplicados automáticamente: cada estudiante aparece una sola vez sin necesidad de validarlo manualmente. Además, para este problema no importa el orden ni la posición de los estudiantes, solo si están inscritos o no. Los conjuntos también traen operaciones como unión, intersección y diferencia, que con listas requerirían ciclos y condiciones adicionales.

**2. Si un estudiante se inscribe dos veces en el mismo curso, ¿qué sucede con la información almacenada?**

No pasa nada: el conjunto ignora el segundo registro y el estudiante sigue apareciendo una sola vez. Python no genera ningún error, simplemente no agrega el elemento porque ya existe. Con una lista, en cambio, el nombre quedaría repetido y el conteo de estudiantes sería incorrecto.

**3. ¿Cuál es la diferencia entre la unión y la diferencia simétrica?**

La **unión** (`A | B`) junta todos los elementos que están en A, en B o en ambos, sin repetirlos. En este caso entrega los 10 estudiantes diferentes. La **diferencia simétrica** (`A ^ B`) entrega solo los elementos que están en uno de los dos conjuntos pero no en ambos, es decir, la unión sin la intersección. En este caso deja por fuera a Laura, Pedro y Sofia, que están en los dos cursos.

**4. ¿En qué situaciones reales sería útil utilizar conjuntos para analizar información?**

- Eliminar correos o registros duplicados en una base de datos.
- Saber qué clientes compraron dos productos distintos (intersección) o solo uno de ellos (diferencia).
- Comparar la lista de asistentes de dos eventos.
- Encontrar usuarios que siguen a dos cuentas en una red social.
- Revisar qué estudiantes entregaron una actividad y cuáles faltan por entregar.
- Verificar permisos o roles comunes entre grupos de usuarios.
